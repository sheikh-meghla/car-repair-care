from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CustomUserSignupSerializer

class SignupAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User created successfully",
                "email": user.email,
                "role": user.role
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
