import uuid
from django.db import models

class News(models.Model):
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
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
  