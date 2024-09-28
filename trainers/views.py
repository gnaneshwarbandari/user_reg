from django.shortcuts import get_object_or_404, redirect
from django.forms import ModelForm
from .models import Trainer
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, FormView, ListView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# create a model form
class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        exclude = ['status']


# Create your views here.
class TrainerFormView(LoginRequiredMixin, FormView):
    form_class = TrainerForm
    template_name = 'trainers/index.html' 
    success_url = reverse_lazy('trainers:trainer_view')

    def form_valid(self, form):
        trainer = form.save()
        trainer_name = trainer.name
        messages.success(self.request, f'Trainer with {trainer_name} created successfully')
        return super().form_valid(form)

# list trainers
class TrainersListView(ListView):
    model = Trainer
    context_object_name = 'data'
    template_name = 'trainers/trainers.html'
    ordering = ['-name']

    def post(self, request, *args, **kwargs):
        # Handle the status change when a checkbox is toggled
        trainer_id = request.POST.get('trainer_id')
        trainer = get_object_or_404(Trainer, id=trainer_id)
        trainer.status = not trainer.status  # Toggle the status
        trainer.save()

        # Redirect to the same page after the status is toggled
        return redirect('trainers:trainer_view') 
    
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by('name')
        return queryset

# view each trainer details
class TrainerDetailView(LoginRequiredMixin, DetailView):
    model = Trainer
    template_name = 'trainers/each_trainer.html'
    context_object_name = 'new'

    def get_object(self):
        trainer_id = self.kwargs.get('pk')
        print(trainer_id)
        return get_object_or_404(Trainer, pk=trainer_id)

# remove trainer
class TrainerDelete(LoginRequiredMixin, DeleteView):
    model = Trainer
    success_url = reverse_lazy('trainer_view')

# edit a trainer
class TrainerEdit(LoginRequiredMixin, UpdateView):
    model = Trainer
    fields = ['name', 'qualification', 'college', 'experience', 'training_exp']
    success_url = reverse_lazy('trainer_view')