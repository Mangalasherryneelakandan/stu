from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
