from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.core.validators import MinValueValidator,RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.


class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    age = models.PositiveIntegerField(validators=[MinValueValidator(5)])
    phone = models.CharField(unique=True,validators=[RegexValidator(r'^\+98\d{10}$',
                                                        message="'Phone number must be entered in the format: +98xxxxxxxxxx")])
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def save(self,*args,**kwargs):

        self.username = f'{self.first_name} {self.last_name}'

    
    def clean(self) -> None:
        super().clean()

        if self.age<5:

            raise ValidationError("Age must be at least 5")
        
    
    class Meta:

        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):

        return self.email



