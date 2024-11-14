from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # link to User model
    vaquero_id = models.CharField(
        max_length=8,
        unique=True,
        #regex validator for exactly 8 digits
        validators=[RegexValidator(r'^\d{8}$', 'Vaquero ID must be exactly 8 digits')]
    )

    def __str__(self):
        return self.user.username
