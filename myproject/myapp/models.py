from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as AuthUser # Django's built-in User model



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Publisher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='book')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    is_available = models.BooleanField(default=True)
    
    # --- COVER IMAGE FIELD ADDED ---
    cover_image = models.ImageField(
        upload_to='book_covers/', 
        null=True,                 # Image is optional
        blank=True                 # Also optional in forms
    )

    def __str__(self):
        return self.title

class Edition(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='edition')
    edition_number = models.PositiveIntegerField()
    release_date = models.DateField()
    pages = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.book.title} - Edition {self.edition_number} ({self.release_date.year})"

class Member(models.Model):
    MEMBER_TYPE_CHOICES = [
        ('STUDENT', 'Student'),
        ('EMPLOYEE', 'Employee'),
    ]
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name='member')
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.get_member_type_display()})"

class IssuedBook(models.Model):
    STATUS_CHOICES = [
        ('REQUESTED', 'Requested'),
        ('ISSUED', 'Issued'),
        ('RETURNED', 'Returned'),
        ('OVERDUE', 'Overdue'),
        ('REJECTED', 'Rejected'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='issued_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='issued_books')
    edition = models.ForeignKey(
        Edition,
        on_delete=models.SET_NULL,
        related_name='issued_books',
        null=True,
        blank=True
    )
    issue_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')

    __original_status = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status != self.__original_status:
            if self.status == 'ISSUED':
                self.book.is_available = False
                self.book.save(update_fields=['is_available'])
            elif self.status in ['RETURNED', 'REJECTED'] and self.__original_status == 'ISSUED':
                if not IssuedBook.objects.filter(book=self.book, status='ISSUED').exists():
                    self.book.is_available = True
                    self.book.save(update_fields=['is_available'])
        self.__original_status = self.status

    def __str__(self):
        return f"{self.book.title} issued to {self.member.user.username} ({self.status})"