from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User as AuthUser 
from .models import Category, Book, Edition, Member, IssuedBook 


def home(request):
    search_query = request.GET.get('search', '').strip()
    
    categories_result = Category.objects.all() 
    books_result = Book.objects.none() 
    

    if request.user.is_authenticated:
        if search_query:
            
            books_result = Book.objects.filter(is_available=True).filter(
                Q(title__icontains=search_query) |
                Q(authors__first_name__icontains=search_query) |
                Q(authors__last_name__icontains=search_query) |
                Q(category__name__icontains=search_query)
            ).distinct()
            
            categories_result = Category.objects.filter( 
                # Categories bhi search query se filter hon
                Q(name__icontains=search_query) |
                Q(books__in=books_result) 
            ).distinct()
        else:
            
            pass 
    else:
       
        books_result = Book.objects.filter(is_available=True).order_by('-id')[:5] 
        categories_result = Category.objects.none() 

    context = {
        'books': books_result, 
        'categories': categories_result, 
        'search_query': search_query,
    }
    return render(request, 'user_side/user_home.html', context)


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip().lower()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        member_type = request.POST.get('member_type', Member.MEMBER_TYPE_CHOICES[0][0]) 

        # Basic Validation
        if not all([username, email, password, password2, first_name, last_name]): 
            messages.error(request, "Please fill all required fields.")
            return redirect('signup')
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        if AuthUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')
        if AuthUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        try:
            created_user = AuthUser.objects.create_user(username=username, email=email, password=password)
            created_user.first_name = first_name
            created_user.last_name = last_name
            created_user.save()

            Member.objects.create(user=created_user, member_type=member_type)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Could not create account: {e}")
            return redirect('signup')
    
    # For GET request
    return render(request, 'library/authentication/signup.html', {'member_types': Member.MEMBER_TYPE_CHOICES})


def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email', '').strip()
        password = request.POST.get('password')

        user = authenticate(request, username=username_or_email, password=password)
        if not user:
            try:
                user_obj_by_email = AuthUser.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj_by_email.username, password=password)
            except AuthUser.DoesNotExist:
                user = None

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('home') # Redirect to home page
            else:
                messages.error(request, "This account is inactive.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username/email or password.")
            return redirect('login')
    return render(request, 'library/authentication/login.html')



@login_required
def user_books_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = Book.objects.filter(category=category, is_available=True)
    context = {
        'books': books,
        'category': category
    }
    return render(request, 'user_side/book_list.html', context) 


@login_required
def user_book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    current_member = None
    already_requested_or_issued = False

    try:
        current_member = request.user.member 
    except Member.DoesNotExist:
        messages.error(request, "Your member profile is not set up. Cannot request books.")
        return redirect('home') 
    except AttributeError:
        messages.error(request, "Could not retrieve your member information.")
        return redirect('home')

    if current_member:
        already_requested_or_issued = IssuedBook.objects.filter(
            member=current_member,
            book=book,
            status__in=['REQUESTED', 'ISSUED']
        ).exists()

    if request.method == 'POST':
        if not book.is_available:
            messages.warning(request, "This book is currently not available.")
            return redirect('user_book_detail', book_id=book.id)
        if already_requested_or_issued:
            messages.warning(request, "You have already requested this book or it is currently issued to you.")
            return redirect('user_book_detail', book_id=book.id)

        edition_to_issue = None
        if hasattr(book, 'edition') and book.edition:
            edition_to_issue = book.edition
        
        issue_date_val = timezone.now()
        return_date_val = (timezone.now() + timedelta(days=14)).date() 

        IssuedBook.objects.create(
            member=current_member,
            book=book,
            edition=edition_to_issue,
            issue_date=issue_date_val,
            return_date=return_date_val,
            status='REQUESTED'
        )
        messages.success(request, 'Book request submitted successfully!')
        return redirect('user_request_status')

    context = {
        'book': book,
        'already_requested_or_issued': already_requested_or_issued
    }
    return render(request, 'user_side/book_detail.html', context) 


@login_required
def user_request_status(request):
    try:
        current_member = request.user.member
        requests = IssuedBook.objects.filter(member=current_member).order_by('-issue_date')
        context = {'requests': requests}
        return render(request, 'user_side/request_status.html', context)
    except Member.DoesNotExist:
        messages.info(request, "You do not have a member profile to view requests.")
        return redirect('home')
    except AttributeError:
        messages.error(request, "Could not retrieve your member information for requests.")
        return redirect('home')