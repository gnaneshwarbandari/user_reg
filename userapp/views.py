from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.forms import ModelForm
from .models import Contact
from studentapp.models import Student
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import AdminRegistrationForm, StudentRegistrationForm
from django.contrib.auth.models import Group
from django.contrib.auth import views as auth_views

# Create your views here.
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin-dashboard'

class StudentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'student-dashboard'

def register_admin(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add the user to the 'Admin' group
            admin_group = Group.objects.get(name='Admin')
            user.groups.add(admin_group)
            login(request, user)  # Automatically log in the user
            return redirect('userapp:login')
    else:
        form = AdminRegistrationForm()
    
    return render(request, 'adminapp/register.html', {'form': form})

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add the user to the 'Student' group
            student_group = Group.objects.get(name='Student')
            user.groups.add(student_group)
            login(request, user)  # Automatically log in the user
            return redirect('userapp:login')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'userapp/register.html', {'form': form})

class CustomLoginView(auth_views.LoginView):
    template_name = 'userapp/login.html'

    def get_success_url(self):
        # Get the authenticated user
        user = self.request.user

        print(user.groups)

        # Check if the user is in the 'Admin' group
        if user.groups.filter(name='Admin').exists():
            return reverse('adminapp:admin_home')  # Redirect Admin users to admin dashboard

        # Check if the user is in the 'Student' group
        elif user.groups.filter(name='Student').exists():
            return reverse('userapp:home')  # Redirect Student users to student dashboard

        # Default fallback if no group match
        return reverse('userapp:home')  # Redirect to home or any default page

def home(request):
    return render(request, 'userapp/index.html')

# def admin_home(request):
#     return render(request, 'adminapp/home.html')

# index view
def index_page(request):
    return render(request, 'userapp/index.html')

# about view
def about_page(request):
    return render(request, 'userapp/about.html')


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


# contact view

def contact(request, template_name='userapp/contact.html'):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        contact_form.save()
        return redirect('index_page')
    return render(request, template_name, {'contact_form': contact_form})


def view_students(request, template_name='userapp/students.html'):
    students_data = Student.objects.order_by('id')

    # students_search filter
    query = request.GET.get("q")
    if query:
        students_data = students_data.filter(
            Q(name__icontains=query) |
            Q(select_course__name__icontains=query) |
            Q(select_batch__batch_number__icontains=query)
        ).distinct()

    paginator = Paginator(students_data, 8)
    page = request.GET.get('page')
    students_page = paginator.get_page(page)

    context = {

        'students_data': students_page
    }
    return render(request, template_name, context)


# each students
def each_student_details(request, stud_id, template_name='userapp/each_stud_details.html'):
    stud = get_object_or_404(Student, pk=stud_id)
    context = {
        'stud': stud
    }
    return render(request, template_name, context)


#password reset
class CustomPasswordResetView(auth_views.PasswordResetView):
    # Custom template for rendering the password reset form
    template_name = 'userapp/password_reset_form.html'
    
    # Custom email template to be used for sending the password reset email
    email_template_name = 'userapp/password_reset_email.html'
    
    # URL to redirect after successful submission of password reset request
    success_url = reverse_lazy('userapp:password_reset_done')
    
    # Optional: Custom subject for the password reset email
    subject_template_name = 'userapp/password_reset_subject.txt'
    
    # Optional: Custom context for rendering the email
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_info'] = 'Some extra information'
        return context
    
# views.py
class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'userapp/password_reset_done.html'

# views.py
class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'userapp/password_reset_confirm.html'
    success_url = reverse_lazy('userapp:password_reset_complete')

# views.py
class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'userapp/password_reset_complete.html'
