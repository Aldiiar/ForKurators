from django.db import models
from django.contrib.auth.models import User
from groups.models import Group

class Kurator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Associate with User model
    photo = models.ImageField(blank=True, null=True)
    department = models.CharField(max_length=500)
    university = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    groups = models.ManyToManyField(Group, related_name='kurator_assigned', blank=True)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
