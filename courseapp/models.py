from django.db import models
from trainers.models import Trainer
from topicapp.models import Topic
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.core.validators import RegexValidator
from shared.constants import COUNTRY_CODES

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=40)
    duration = models.PositiveIntegerField(validators=[MinValueValidator(30), MaxValueValidator(200)])
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    fees = models.PositiveIntegerField(validators=[MinValueValidator(5000), MaxValueValidator(80000)])
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is new (doesn't exist in the DB yet)
            self.status = True  # Set status to active by default
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_update', kwargs={'pk': self.pk})
