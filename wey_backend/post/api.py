from django.http import JsonResponse

from .models import Post, User
from .serializers import PostSerializer
from .forms import PostForm
from account.serializers import UserSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.


# หน้า feed
@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()  # change later to feed
    
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

# ขั้นตอนที่ฟังก์ชันทำได้คือ:

# Post.objects.all() ใช้สำหรับดึงข้อมูลทั้งหมดจากโมเดล Post ในฐานข้อมูล 
# และเก็บลงในตัวแปร posts
# PostSerializer(post, many=True) ใช้สร้างออบเจ็กต์ Serializer 
# สำหรับข้อมูลโพสต์ที่ได้จากขั้นตอนที่ 1 โดยกำหนด many=True 
# เนื่องจากเราต้องการซีเรียลไซซ์รายการของโพสต์ทั้งหมด
# JsonResponse({'data': serializer.data}) สร้างออบเจ็กต์ JsonResponse 
# โดยส่งข้อมูลในรูปแบบ JSON ซึ่งมีโครงสร้างของข้อมูลอยู่ในคีย์ 'data' 
# และค่าข้อมูลเป็นผลลัพธ์จากการซีเรียลไซซ์ที่ได้จากขั้นตอนที่ 2
# โดยผลลัพธ์ที่ได้จากฟังก์ชัน post_list จะเป็น JSON 

# JsonResponse: เป็นฟังก์ชันใน Django ที่ใช้สร้างตัวอ็อบเจกเกอร์ 
# JsonResponse ที่จะถูกส่งกลับไปยัง client
# serializer.data: เป็นข้อมูลที่ได้จากการแปลง (serialize) 
# โมเดลหรืออ็อบเจกต์ให้กลายเป็นรูปแบบ JSON
# safe=False: กำหนดให้ JsonResponse สามารถรับข้อมูลที่ไม่ใช่รูปแบบ JSONs


# show the post where field created_by (id) at feed
@api_view(['GET'])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)
    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)
       
    return JsonResponse({
        'posts': posts_serializer.data, 
        'user': user_serializer.data
        }, safe=False)  


# created post
@api_view(['POST'])
def post_create(request):
    data = request.data
    # print(data)
    form = PostForm(request.data)
    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user  # มีการกำหนดค่าเพิ่มก่อน save form
        post.save()
        
        serializer = PostSerializer(post)
        
        return JsonResponse(serializer.data, safe=False)
    else:  
        return JsonResponse({'error': 'add something here later!'})

# post = form.save(commit=False) ในที่นี้หมายถึงการบันทึกข้อมูลจากฟอร์ม (form) 
# ลงในโมเดล (model) โดยใช้เมธอด save() แต่กำหนด commit=False 
# เพื่อบอกว่าไม่ต้องบันทึกข้อมูลลงในฐานข้อมูลทันที 
# แต่ให้สร้างอ็อบเจกต์ของโมเดลก่อนและกำหนดค่าข้อมูลให้กับอ็อบเจกต์นั้นก่อน 
# ซึ่งในที่นี้เป็นตัวแปร post ที่ถูกสร้างขึ้นมาจากโมเดลที่เกี่ยวข้องกับฟอร์ม
