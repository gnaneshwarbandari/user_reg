from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .adminforms import RegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, FormView

# Create your views here.

class RegisterView(FormView):
    template_name = 'adminapp/register.html'  # Path to your template
    form_class = RegisterForm  # Your custom registration form
    success_url = reverse_lazy('userapp:login')  # Redirect after successful registration

    def form_valid(self, form):
        # Save the form to create the new user
        form.save()

        # Get the username from the form data
        username = form.cleaned_data.get('username')

        # Send a success message to the user
        messages.success(self.request, f'Account created for {username}!')

        # Call the superclass's form_valid method to handle the redirect
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # You can add custom logic here if the form is invalid
        return super().form_invalid(form)


class AdminHomeView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'adminapp/home.html'

    # This method restricts the access to users in the 'Admin' group
    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

    # Handle unauthorized access (users who are not Admin)
    def handle_no_permission(self):
        return redirect('userapp:no-access')  # Redirect to a "no access" page or login page

