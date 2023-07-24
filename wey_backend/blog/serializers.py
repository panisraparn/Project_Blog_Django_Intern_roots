from rest_framework import serializers
from .models import Blog, Topic


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'
        depth = 2


class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = '__all__'
        depth = 2


class UpdateTopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = '__all__'
        
