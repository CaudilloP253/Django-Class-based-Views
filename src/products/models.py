from django.db import models
from django.conf import settings

User=settings_AUTH_USER_MODEL
class Product(models.Model):
    user = models.ForeingKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug= models.SlugField(unique=True)

class DigitalProduct(Product):
    class Meta:
        proxy = True
