from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Main home page

    path('category/<int:category_id>/', views.user_books_by_category, name='user_books_by_category'),
    path('book/<int:book_id>/', views.user_book_detail, name='user_book_detail'),
    path('requests/', views.user_request_status, name='user_request_status'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]