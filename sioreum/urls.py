from django.urls import path
from . import views

urlpatterns = [
    path('', views.poetList, name='poetList'),
    path('poet', views.poetList, name='poetList'),
    path('poet/<int:pk>/', views.poetDetail, name='poetDetail'),
]
