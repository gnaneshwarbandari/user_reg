from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('home/', views.AdminHomeView.as_view(), name='admin_home'),
]
