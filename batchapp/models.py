from django.db import models
from courseapp.models import Course

class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=20)
    start_date = models.DateField()  # No 'widget', 'required', or 'label' here
    end_date = models.DateField()    # No 'widget', 'required', or 'label' here
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is new (doesn't exist in the DB yet)
            self.status = True  # Set status to active by default
        super(Batch, self).save(*args, **kwargs)