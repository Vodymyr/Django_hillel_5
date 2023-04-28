from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    subjects = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
