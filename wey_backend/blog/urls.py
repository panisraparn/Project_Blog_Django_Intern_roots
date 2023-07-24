from django.urls import path
from rest_framework import routers
from . import views
from django.urls import include
from . import api

router = routers.DefaultRouter()
router.register(r'topic', views.TopicViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
    path('topic/delete/<id>/', api.topic_delete,
         name='topic_delete'),
    path('topic/update/<id>/', api.topic_update,
         name='topic-update')
]
