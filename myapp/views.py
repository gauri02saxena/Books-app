from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import RegisterSerializer

import logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"New user registered: {serializer.validated_data['username']}")
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
    logger.error(f"User registration failed: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    books = Book.objects.all()
    logger.info(f"Fetched {len(books)} book(s).")
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_book(request):
    is_many = isinstance(request.data, list)
    serializer = BookSerializer(data=request.data, many=is_many)

    if serializer.is_valid():
        serializer.save()
        logger.info(f"{'Multiple books' if is_many else 'Book'} created successfully.")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    logger.error(f"Failed to create {'books' if is_many else 'book'}: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        logger.warning(f"[404] Update failed: Book with id={pk} not found.")
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Book with id={pk} updated successfully.")
        return Response(serializer.data)

    logger.error(f"Failed to update book with id={pk}: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        logger.warning(f"[404] Partial update failed: Book with id={pk} not found.")
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Book with id={pk} partially updated successfully.")
        return Response(serializer.data)

    logger.error(f"Failed to partially update book with id={pk}: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        logger.warning(f"[404] Delete failed: Book with id={pk} not found.")
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    book_title = book.title
    book.delete()
    logger.info(f"Book deleted successfully: [id={pk}, title='{book_title}']")
    return Response({"message": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
