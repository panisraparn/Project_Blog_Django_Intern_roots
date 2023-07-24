from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('account.urls')),
    path('api/posts/', include('post.urls')),
    path('api/blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
