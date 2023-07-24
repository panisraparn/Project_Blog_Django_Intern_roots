import uuid
from django.db import models
from account.models import User

from django.utils.timesince import timesince
# Create your models here.


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(User, related_name='post_attachments',
                                   on_delete=models.CASCADE)

    # def get_image(self):
    #     if self.image:
    #         return settings.WEBSITE_URL + self.image.url
    #     else:
    #         return ''


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    
    attachments = models.ManyToManyField(PostAttachment, blank=True)
    
    # like
    # like_count
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts',
                                   on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
    
    def created_at_formatted(self):
        return timesince(self.created_at)
    
       
# created_at_formatted 
# เป็นเมธอดในคลาส User 
# ที่ใช้สำหรับการแสดงผลวันที่และเวลาที่สร้างของผู้ใช้งานในรูปแบบที่ถูกจัดรูปแบบ

# เมธอดนี้ใช้ฟังก์ชัน timesince 
# เพื่อคำนวณเวลาที่ผ่านไปตั้งแต่วันที่และเวลาที่สร้างของผู้ใช้งานจนถึงปัจจุบัน 
# และคืนค่าเป็นข้อความที่แสดงผลเป็นรูปแบบของเวลาที่ผ่านไป 
# (เช่น "2 minutes ago", "3 days ago", "1 year ago" เป็นต้น)
