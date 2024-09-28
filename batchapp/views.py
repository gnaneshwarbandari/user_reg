from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Batch
from .batch_form import BatchForm
from django.views.generic import UpdateView, DeleteView, FormView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
   
# create batch
class BatchFormView(LoginRequiredMixin, FormView):
    form_class = BatchForm
    template_name = 'batchapp/give_batch.html' 
    success_url = reverse_lazy('batchapp:batch')

    def form_valid(self, form):
        batch = form.save()
        num = batch.batch_number
        messages.success(self.request, f'{num} batch created successfully')
        return super().form_valid(form)

# list batches
class BatchListView(LoginRequiredMixin, ListView):
    model = Batch
    template_name = 'batchapp/batches.html'
    context_object_name = 'batches'

    def post(self, request, *args, **kwargs):
        # Handle the status change when a checkbox is toggled
        batch_id = request.POST.get('batch_id')
        batch = get_object_or_404(Batch, id=batch_id)
        batch.status = not batch.status  # Toggle the status
        batch.save()

        # Redirect to the same page after the status is toggled
        return redirect('batchapp:batch_list') 
    
    def get_queryset(self):
        queryset = super().get_queryset().all()
        return queryset

# each batches
class BatchDetailView(LoginRequiredMixin, DetailView):
    model = Batch
    template_name = 'batchapp/batch_details.html'
    context_object_name = 'each_bch'

    def get_object(self):
        batch_id = self.kwargs.get('batch_id')
        return get_object_or_404(Batch, pk=batch_id)

# delete a course
class BatchDelete(LoginRequiredMixin, DeleteView):
    model = Batch
    success_url = reverse_lazy('batchapp:batch_list')

# update batch
class BatchEdit(LoginRequiredMixin, UpdateView):
    model = Batch
    fields = '__all__'
    success_url = reverse_lazy('batchapp:batch_list')
