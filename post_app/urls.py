from django.urls import path

from post_app.views import PostList, CreatePost, CategoryList, GetOnePost, PostDetailUpdate, PostDetailDelete,\
    GePublishedPosts, GeNotPublishedPosts


urlpatterns = [
    path('create/post/', CreatePost.as_view()),

    path('post/<int:pk>/', GetOnePost.as_view()),
    path('post/<int:pk>/update/', PostDetailUpdate.as_view()),
    path('post/<int:pk>/delete/', PostDetailDelete.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/published/', GePublishedPosts.as_view()),
    path('posts/npublished/', GeNotPublishedPosts.as_view()),

    path('categories/', CategoryList.as_view()),

]