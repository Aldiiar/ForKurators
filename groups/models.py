from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=255)
    # kurator = models.OneToOneField()

    def __str__(self):
        return self.group_name



class Student(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_b = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"
