from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.crud import BookViewSet, AuthorViewSet
from myapp.views.auth import RegisterView
from .views.filters import BookDynamicFilterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'authors', AuthorViewSet, basename='authors')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('books/filter/', BookDynamicFilterView.as_view(), name='book-dynamic-filter'),
    path('', include(router.urls)),
]
