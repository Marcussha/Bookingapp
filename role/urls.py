from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create',views.create, name="create"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.clear, name="delete")

] 