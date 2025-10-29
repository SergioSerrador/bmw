from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    propic = models.ImageField(upload_to="media/", default="media/default.png", blank=True)
    
    def __str__(self):
        return self.name
    
class Group(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
