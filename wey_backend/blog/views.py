from django.shortcuts import render, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from .models import Blog, Topic
from .serializers import BlogSerializer, TopicSerializer
from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.


# def blog_list(request):
    
#     # get all articles
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TodoSerializer(data=data)
#         if serializer.isvalid():
#             serializer.save()
#             return JsonResponse(serialize.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
 
 
# @csrf_exempt
# def todo_details(request, pk):
#     try:
#         todo = Todo.objects.get(pk=pk)
        
#     except Todo.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = TodoSerializer(todo)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = TodoSerializer(todo, data=data)
#         if serializer.isvalid():
#             serializer.save()
#             return JsonResponse(serialize.data)
#         return JsonResponse(serializer.errors)
    
#     elif request.method == 'DELETE':
#         todo.delete()
#         return HttpResponse(status=204)
 
     
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.OrderingFilter, 
        filters.SearchFilter,
    ]
    filterset_fields = "__all__"
    search_fields = ("title")
    
    
class TopicViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.OrderingFilter, 
        filters.SearchFilter,
    ]
    filterset_fields = "__all__"
    search_fields = ("name")
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        return Response(serializer.data)
    
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance,
    #                                      data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         instance._prefetched_objects_cache = {}

    #     return Response(serializer.data)
    
    # def perform_update(self, serializer):
    #     serializer.save()
    
    # def destroy(self, request, *args, **kwargs):
    #     topic = self.get_object()
    #     topic.is_active = False
    #     topic.save()
    #     return Response(data='delete success')
    
    
