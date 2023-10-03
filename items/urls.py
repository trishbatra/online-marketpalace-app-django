from django.urls import path
from . import views

app_name = 'items'
urlpatterns = [
    path("", views.itemss , name="itemss" ),
    path("add/", views.addI , name="add" ),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete', views.delete, name="delete"),
    path('<int:pk>/edit', views.editI, name="edit"),
]
