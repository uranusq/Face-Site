from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos", default="def_photo/15.jpg", blank=True)
    description = models.TextField()

    def __str__(self):
        return str(self.name)+ " " + str(self.last_name)

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default="None")
    photo = models.ImageField(upload_to="image", default="def_photo/15.jpg", blank=True)
    description = models.TextField()

    def __str__(self):
        return str(self. project_name)