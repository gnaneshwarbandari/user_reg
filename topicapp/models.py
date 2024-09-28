from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from shared.constants import TOPICS

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=40, choices=TOPICS)
    duration = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(80)])
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.topic_name
    
    def save(self, *args, **kwargs):
        super(Topic, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        print(self.pk)
        return reverse('each_topic', kwargs={'pk': self.pk})
