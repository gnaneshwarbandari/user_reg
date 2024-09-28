from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Course
from django.views.generic import UpdateView, DeleteView, FormView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['status']

# Create your views here.
class CoursesFormView(LoginRequiredMixin,FormView):
    form_class = CourseForm
    template_name = 'courseapp/course.html' 
    success_url = reverse_lazy('courseapp:course_create')
    login_url = '/login/'

    def form_valid(self, form):
        course = form.save()
        num = course.title
        messages.success(self.request, f'{num} course created successfully')
        return super().form_valid(form)
    
# course list
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courseapp/courselist.html'
    context_object_name = 'course'

    def post(self, request, *args, **kwargs):
        # Handle the status change when a checkbox is toggled
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        course.status = not course.status  # Toggle the status
        course.save()

        # Redirect to the same page after the status is toggled
        return redirect('courseapp:course_list') 
    
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by('title')
        return queryset
    
# each courses
class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'courseapp/course_details.html'
    context_object_name = 'each_one'

    def get_object(self):
        course_id = self.kwargs.get('course_id')
        return get_object_or_404(Course, pk=course_id)

# delete a course
class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courseapp:course_list')

# update a course
class CourseEdit(LoginRequiredMixin, UpdateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('courseapp:course_list')

