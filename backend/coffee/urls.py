from django.urls import path,include
from rest_framework import routers

from . import views


urlpatterns=[
    path('category/',views.CategoryListCreateAPIView.as_view()),
    path('staff/',views.StaffListCreateAPIView.as_view()),
    path('table/',views.TableListCreateAPIView.as_view()),
    path('menu/<str:category_name>/',views.MenuCategoryListCreateAPIView.as_view()),
    path('menu/',views.MenuCategoryListCreateAPIView.as_view()),

    path('category/<int:pk>/',views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('staff/<int:pk>/',views.StaffRetrieveUpdateDestroyAPIView.as_view()),
    path('table/<int:pk>/',views.TableRetrieveUpdateDestroyAPIView.as_view()),
    path('menu/<int:pk>',views.MenuRetrieveUpdateDestroyAPIView.as_view()),
]

