from django.shortcuts import get_object_or_404, redirect
from django.forms import ModelForm
from django.contrib import messages
from .models import Topic
from django.views.generic import UpdateView, DeleteView, FormView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        exclude = ['status']


# create topic
class TopicFormView(LoginRequiredMixin, FormView):
    form_class = TopicForm
    template_name = 'topicapp/give_topic.html' 
    success_url = reverse_lazy('topicapp:topic')

    def form_valid(self, form):
        topic = form.save()
        num = topic.topic_name
        messages.success(self.request, f'{num} topic created successfully')
        return super().form_valid(form)

# list topics
class TopicListView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = 'topicapp/topics.html'
    context_object_name = 'topics'

    def post(self, request, *args, **kwargs):
        # Handle the status change when a checkbox is toggled
        topic_id = request.POST.get('topic_id')
        topic = get_object_or_404(Topic, id=topic_id)
        topic.status = not topic.status  # Toggle the status
        topic.save()

        # Redirect to the same page after the status is toggled
        return redirect('topicapp:topic_list') 
    
    def get_queryset(self):
        queryset = super().get_queryset().all()
        return queryset

# each topics
class TopicDetailView(LoginRequiredMixin, DetailView):
    model = Topic
    template_name = 'topicapp/topic_details.html'
    context_object_name = 'each_tpk'

    def get_object(self):
        topic_id = self.kwargs.get('topic_id')
        print(topic_id)
        return get_object_or_404(Topic, pk=topic_id)

# delete Topic
class TopicDelete(LoginRequiredMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy('topicapp:topic_list')

# update Topic
class TopicEdit(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = '__all__'
    success_url = reverse_lazy('topicapp:topic_list')
