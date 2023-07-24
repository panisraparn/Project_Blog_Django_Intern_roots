from django.forms import ModelForm

from .models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('body', 'topic')


class TopicForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('name',)
