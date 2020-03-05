from django.contrib import admin
from django.urls import path
from newapp.views import home, create, update, delete

urlpatterns = [
    path('home', home, name='home'),
    path('create', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>', delete, name='delete')
]
