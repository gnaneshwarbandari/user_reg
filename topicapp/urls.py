from django.urls import path
from . import views

app_name = "topicapp"
urlpatterns = [
    path('', views.TopicFormView.as_view(), name='topic'),
    path('topics/', views.TopicListView.as_view(), name='topic_list'),
    path('<int:topic_id>', views.TopicDetailView.as_view(), name='each_topic'),
    path('delete/<int:pk>', views.TopicDelete.as_view(), name='topic_delete'),
    path('edit/<int:pk>', views.TopicEdit.as_view(), name='edit_topic'),
]


