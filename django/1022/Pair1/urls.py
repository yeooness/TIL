from django.contrib import admin
from django.urls import path
from . import views

app_name = "Pair1"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("index/<int:pk>", views.index1, name="index1"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("update/<int:pk>", views.update, name="update"),
]
