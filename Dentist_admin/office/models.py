from django.db import models

# Create your models here.
# Define a new class named 'Patient' that inherits from models.Model.
# 'models.Model' is the base class that gives your class all the
# functionality of a Django model, like database table creation and
# object management.
class  Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):

        return f"{self.first_name} {self.last_name} is {self.age} years old."