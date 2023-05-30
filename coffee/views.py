from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets,status

from .models import Menu,Category,Table,Staff
from .serializers import CategorySerializer,TableSerializer,StaffSerializer,MenuSerializer
from .permissions import IsUserOrIsAdmin


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsUserOrIsAdmin]


class TableListCreateAPIView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsUserOrIsAdmin]


class StaffListCreateAPIView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsUserOrIsAdmin]


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsUserOrIsAdmin]


class TableRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsUserOrIsAdmin]


class StaffRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsUserOrIsAdmin]


class MenuCategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        if category_name:
            return Menu.objects.filter(category__name=category_name)
        else:
            return Menu.objects.all()

    def perform_create(self, serializer):
        category_name = self.kwargs.get('category_name')
        category = None
        if category_name:
            category = Category.objects.get(name=category_name)
        else:
            category=get_object_or_404(Category,pk=self.request.data.get('category'))
        serializer.save(category=category)
    permission_classes = [IsUserOrIsAdmin]


class MenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsUserOrIsAdmin]


