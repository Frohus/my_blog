from django.db.models import Q

from .models import Post
import django_filters


class PostFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='filter', label='Search posts')

    class Meta:
        model = Post
        fields = ['q']

    def filter(self, queryset, name, value):
        return Post.objects.filter(Q(title__icontains=value) | Q(content__icontains=value))
