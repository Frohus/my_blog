from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


class PostsView(ListView):
    queryset = Post.objects.all()
    # model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-post_date_posted']
    paginate_by = 10
