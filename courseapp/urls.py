from django.urls import path
from . import views

app_name = "courseapp"

urlpatterns = [
    path('', views.CoursesFormView.as_view(), name='course_create'),
    path('course/', views.CourseListView.as_view(), name='course_list'),
    path('<int:pk>', views.CourseDetailView.as_view(), name='each_courses'),
    path('delete/<int:pk>', views.CourseDelete.as_view(), name='course_delete'),
    path('edit/<int:pk>', views.CourseEdit.as_view(), name='course_edit'),
]

