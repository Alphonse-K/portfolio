from django.urls import path
from blog.views import PostDetailView, CommentUpdateView, LikesIncrementView


app_name = 'blog'

urlpatterns = [
    path('blog/<int:pk>/', PostDetailView.as_view(), name='blogpost'),
    path('blog/comment/update/<int:pk>/', CommentUpdateView.as_view(), name='comment'),
    path('blog/likes/<int:pk>/', LikesIncrementView.as_view(), name='likes')
]
