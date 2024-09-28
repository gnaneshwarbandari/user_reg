from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from shared.constants import COUNTRY_CODES

def validate_gmail(email):
    if not email.endswith('@gmail.com'):
        raise ValidationError("Email must be a Gmail address.")
    if Trainer.objects.filter(email=email).exists():
        raise ValidationError("This email is already registered.")

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=25)
    qualification = models.CharField(max_length=10)
    college = models.CharField(max_length=30)
    experience = models.PositiveIntegerField(validators=[MinValueValidator(3), MaxValueValidator(50)])
    training_exp = models.PositiveIntegerField(validators=[MinValueValidator(3), MaxValueValidator(50)])
    email = models.EmailField(max_length=60, validators=[validate_gmail])
    country_code = models.CharField(max_length=3, choices=COUNTRY_CODES, default='+91')
    
    phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Mobile number must be exactly 10 digits.')],
        help_text='Enter a valid 10-digit mobile number',
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Trainer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('trainer_one', kwargs={'pk': self.pk})
