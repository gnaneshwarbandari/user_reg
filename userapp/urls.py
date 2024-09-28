# userapp/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'userapp'
urlpatterns = [
    path('main/', views.register_admin, name='register-admin'),
    path('student/', views.register_student, name='register-student'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name='logout'),
    path('no-access/', views.TemplateView.as_view(template_name='userapp/no_access.html'), name='no-access'),

    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', views.home, name='home'),  # Home URL for students
    path('home/', views.index_page, name='index_page'),  # Home URL for students
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact, name='contact'),
    path('view_students/', views.view_students, name='view_students'),
    path('<int:stud_id>', views.each_student_details, name='each_student_details'),
]
