import uuid
from django.db import models
from django.contrib.auth.models import User


class Produk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    CATEGORY_CHOICES = [
        ('boots', 'Boots'),
        ('knee-guards', 'Knee-guards'),
        ('footballs', 'Footballs'),
        ('socks', 'Socks'),
        ('shirts', 'Shirts'),
        ('gloves', 'Gloves'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='boots')
    thumbnail = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products_views = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_product_hot = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.products_views += 1
        self.save()
    
    @property
    def is_product_hot(self):
        return self.products_views > 20
    
