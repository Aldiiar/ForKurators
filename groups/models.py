from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=255)
    department = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.group_name



class Student(models.Model):
    photo = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_b = models.DateField()
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"
