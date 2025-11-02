from django.db import models
from django.contrib.auth.models import User
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

COCHES = [
    ('Ber', 'Berlina'),
    ('SUV', 'SUV'),
    ('Cou', 'Coupé'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=3, choices=COCHES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}, by {self.user}"