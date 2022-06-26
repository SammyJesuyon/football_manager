from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(
                    data={
                        "message": "error",
                        "data": "Ensure email and password are correct",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if user.check_password(password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response(
                        data={
                            "token": token.key,
                            "success": "You've successfully Logged in",  
                        },
                        status=status.HTTP_200_OK,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        request.user.auth_token.delete()
        return Response(data={"success": "You've been logged out"}, status=status.HTTP_200_OK)
