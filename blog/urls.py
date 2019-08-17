from django.urls import path
from .views import PostsView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns =[
    path('', PostsView.as_view(), name='homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]