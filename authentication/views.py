from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# Регистрация
class RegistrationAPIView(CreateAPIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        token = Token.objects.create(user_id=user.id)
        return Response({'username': user.username, 'password': user.password, 'token': token.key}, status=status.HTTP_201_CREATED)

    
