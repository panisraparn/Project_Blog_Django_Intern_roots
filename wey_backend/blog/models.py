import uuid
from django.db import models
from account.models import User


# Create your models here.

class Topic(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='blog',
                                   on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    
    class Meta:
        # เรียงจากน้อยไปมาก
        ordering = ['-updated_at', '-created_at']
        
    def __str__(self):
        return f'{self.title}_{self.id}'
