from django.urls import path
from . import views
from django.contrib.auth import views as auth_V
from .forms import loginForm
app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signUP, name="signup"),
    path('login/', auth_V.LoginView.as_view(template_name='core/login.html', authentication_form= loginForm), name="login")
]
