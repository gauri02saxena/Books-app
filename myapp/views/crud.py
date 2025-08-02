from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from ..serializers import BookSerializer
from ..models import Book
from ..models import Author
from ..serializers import AuthorSerializer
from .filters import BookFilter
import logging
logger = logging.getLogger(__name__)

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Book model.
    Includes filtering support via DjangoFilterBackend.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    def create(self, request, *args, **kwargs):
        """
        Create one or more Book records.
        """
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        logger.info(f"Book updated successfully.")
        return serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        title = instance.title
        self.perform_destroy(instance)
        return Response(
            {"message": f"Book deleted successfully: [title='{title}']"},
            status=status.HTTP_200_OK
        )

class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Author model.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


