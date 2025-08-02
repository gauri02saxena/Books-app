from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import RegisterSerializer
import logging

logger = logging.getLogger(__name__)

class RegisterView(APIView):
    """
    Handles user registration via POST.
    """
    def post(self, request):
        """
        Registers a new user if data is valid.
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"New user registered: {serializer.validated_data['username']}")
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        logger.error(f"User registration failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
