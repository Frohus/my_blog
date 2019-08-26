from django.urls import path
from .views import (PostsView,
                    PostCreateView,
                    PostDetailView,
                    PostUpdateView,
                    PostDeleteView,
                    add_comment_to_post,
                    comment_approve,
                    comment_remove,)

urlpatterns =[
    path('', PostsView.as_view(), name='homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', add_comment_to_post, name="add_comment_to_post"),
    path('comment/<int:pk>/approve/', comment_approve, name="comment-approve"),
    path('comment/<int:pk>/remove/', comment_remove, name="comment-remove"),
]