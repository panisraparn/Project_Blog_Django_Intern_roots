# from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Topic
from rest_framework.response import Response
from .serializers import TopicSerializer, UpdateTopicSerializer
from rest_framework import status


from rest_framework.decorators import api_view


@api_view(['DELETE'])
def topic_delete(request, id):
    
    topic = get_object_or_404(Topic, id=id)
    topic.delete()
    
    return Response(data='delete success')


@api_view(['PUT'])
def topic_update(request, id):
    topic = get_object_or_404(Topic, id=id)

    # สร้างตัวแปร serializer โดยใช้ TopicSerializer และ instance topic
    serializer = UpdateTopicSerializer(instance=topic, data=request.data)

    if serializer.is_valid():
        serializer.save()  # ทำการอัปเดตข้อมูล

        return Response(data='update success')
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def blog_detail(request, id):
#     # user = User.objects.get(pk=id)
#     # posts = Post.objects.filter(created_by_id=id)
    
#     topic = Topic.objects.get(pk=id)
#     # posts_serializer = PostSerializer(posts, many=True)
#     # user_serializer = UserSerializer(user)
#     topic_serializer = TopicSerializer(topic)
       
#     return JsonResponse({
#         'topic': topic_serializer.data
#         # 'posts': posts_serializer.data, 
#         # 'user': user_serializer.data
#         }, safe=False)  
