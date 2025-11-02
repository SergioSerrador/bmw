from django.contrib import admin
from .models import Person, Product
# Register your models here.

admin.site.register(Person)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'user', 'date_published')