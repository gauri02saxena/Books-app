from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_user


urlpatterns = [
    path('auth/register/', register_user, name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('books/', views.get_books, name='get_books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/update/<int:pk>/', views.update_book, name='update_book'),
    path('books/partial-update/<int:pk>/', views.partial_update_book, name='partial_update_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]
