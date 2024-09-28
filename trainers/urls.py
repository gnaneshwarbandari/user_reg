from django.urls import path
from . import views

app_name = "trainers"
urlpatterns = [
    path('', views.TrainerFormView.as_view(), name='trainer_create'),
    path('trainers/', views.TrainersListView.as_view(), name='trainer_view'),
    path('<int:pk>', views.TrainerDetailView.as_view(), name='trainer_one'),
    path('delete/<int:pk>', views.TrainerDelete.as_view(), name='trainer_delete'),
    path('edit/<int:pk>', views.TrainerEdit.as_view(), name='trainer_edit'),
]
