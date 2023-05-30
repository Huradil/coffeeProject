from rest_framework import generics
from .permissions import IsSuperuser

from .models import User
from .serializers import UserSerializer,UserForChange


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserForChange
    permission_classes = [IsSuperuser]


