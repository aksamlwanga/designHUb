from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class Tenant(models.Model):
    name=models.CharField(max_length=40)
    id_no=models.IntegerField(
         null=True,
         validators=[
            MinValueValidator(10)
        ])
    telephone=PhoneNumberField(null=False, blank=False)
    company= models.CharField(max_length=40)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class Temperature(models.Model):
     temperature=models.DecimalField(max_digits=5, decimal_places=2)
     userTempId=models.ForeignKey(Tenant,on_delete=models.CASCADE)
     date_posted=models.DateTimeField(default=timezone.now)
    #  def __str__(self):
    #     return str(self.temperature)