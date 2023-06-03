from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(blank=True, upload_to=".")
    
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(max_length=100, blank=True)
    count = models.IntegerField(default=0, blank=True)
    availability = models.BooleanField(default=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

