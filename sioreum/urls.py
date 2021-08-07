from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('poet', views.poetList, name='poetList'),
    path('poet/<int:pk>/', views.poetDetail, name='poetDetail'),
    path('visitor', views.visitList, name='visitList'),
    path('visitor/write/', views.visitCreate, name='write'),
]