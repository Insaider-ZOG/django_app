from django.urls import path

from post_app.views import PostList, CreatePost, CategoryList, PostUpdate, OnePostDetail


urlpatterns = [
    path('post/<int:pk>/update', PostUpdate.as_view()),
    path('post/<int:pk>', OnePostDetail.as_view()),
    path('posts/', PostList.as_view()),
    path('create/post/', CreatePost.as_view()),

    path('categories/', CategoryList.as_view()),

]