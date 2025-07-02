from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User as AuthUser
from django.utils import timezone # timezone import kiya
from datetime import timedelta    # timedelta import kiya
from django.contrib import messages # messages import kiya


from .models import Category, Author, Publisher, Book, Edition, Member, IssuedBook



class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'Member Profile'
    fk_name = 'user'

class CustomUserAdmin(BaseUserAdmin):
    inlines = (MemberInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_member_type_display_for_admin')
    list_select_related = ('member',)

    def get_member_type_display_for_admin(self, instance):
        try:
            if hasattr(instance, 'member') and instance.member:
                 return instance.member.get_member_type_display()
        except Member.DoesNotExist:
            return None
        return 'N/A'
    get_member_type_display_for_admin.short_description = 'Member Type'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'publisher_display', 'is_available']
    search_fields = ['title', 'authors__first_name', 'authors__last_name', 'category__name']
    list_filter = ['category', 'is_available', 'authors']
    filter_horizontal = ('authors',)

    def publisher_display(self, obj):
        if obj.publisher:
            return f"{obj.publisher.first_name} {obj.publisher.last_name}"
        return None
    publisher_display.short_description = 'Publisher'

class EditionAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'edition_number', 'release_date', 'pages']
    list_filter = ['release_date', 'book']
    search_fields = ['book__title']

    def book_title(self, obj):
        return obj.book.title
    book_title.short_description = 'Book Title'
    book_title.admin_order_field = 'book__title'

class MemberAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'member_type', 'get_user_email']
    search_fields = ['user__username', 'user__email']
    list_filter = ['member_type']
    list_select_related = ('user',)

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user__username'

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'Email'
    get_user_email.admin_order_field = 'user__email'

# --- Updated IssuedBookAdmin ---
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ['book_title_display', 'edition_info', 'member_username', 'issue_date', 'return_date', 'status', 'actual_return_date']
    list_filter = ['status', 'member__member_type', 'issue_date', 'return_date']
    search_fields = ['book__title', 'member__user__username', 'edition__edition_number']
    list_select_related = ('book', 'edition', 'member', 'member__user')
    autocomplete_fields = ['member', 'book', 'edition']
    
    actions = ['approve_selected_requests', 'reject_selected_requests', 'mark_as_returned_admin']

    def book_title_display(self, obj):
        return obj.book.title
    book_title_display.short_description = 'Book'
    book_title_display.admin_order_field = 'book__title'

    def edition_info(self, obj):
        if obj.edition:
            return f"Ed. {obj.edition.edition_number}"
        return "N/A"
    edition_info.short_description = 'Edition'

    def member_username(self, obj):
        return obj.member.user.username
    member_username.short_description = 'Member'
    member_username.admin_order_field = 'member__user__username'

    # --- Custom Actions ---
    def approve_selected_requests(self, request, queryset):
        updated_count = 0
        for req in queryset.filter(status='REQUESTED'): # Sirf 'REQUESTED' status wali requests ko approve karein
            if req.book.is_available: # Check karein ke book abhi bhi available hai
                req.status = 'ISSUED'
                
                if not req.return_date: # Agar return_date set nahi hai
                    req.return_date = (timezone.now() + timedelta(days=14)).date() # Example: 14 din
                
                req.save() 
                updated_count += 1
            else:
                self.message_user(request, f"Book '{req.book.title}' is no longer available to issue for request by {req.member.user.username}.", level=messages.WARNING)
        
        if updated_count > 0:
            self.message_user(request, f"{updated_count} request(s) successfully approved and marked as ISSUED.")
    approve_selected_requests.short_description = "Approve selected requests (Set to ISSUED)"

    def reject_selected_requests(self, request, queryset):
        
        updated_count = queryset.filter(status='REQUESTED').update(status='REJECTED')
        
        if updated_count > 0:
            self.message_user(request, f"{updated_count} request(s) successfully REJECTED.")
    reject_selected_requests.short_description = "Reject selected requests"

    def mark_as_returned_admin(self, request, queryset):
        updated_count = 0
        for req in queryset.filter(status='ISSUED'): # Sirf 'ISSUED' status wali books ko returned mark karein
            req.status = 'RETURNED'
            req.actual_return_date = timezone.now().date() # Aaj ki date
            req.save() # Model ka overridden save() method call hoga (book availability update ke liye)
            updated_count += 1
        if updated_count > 0:
            self.message_user(request, f"{updated_count} book(s) successfully marked as RETURNED.")
    mark_as_returned_admin.short_description = "Mark selected ISSUED books as RETURNED"

# --- Register Models with Admin Site ---
if admin.site.is_registered(AuthUser):
    admin.site.unregister(AuthUser)
admin.site.register(AuthUser, CustomUserAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Edition, EditionAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(IssuedBook, IssuedBookAdmin)