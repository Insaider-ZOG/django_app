from django.urls import path

from comment_app.views import CreateComment, CommentUpdate, OneComment


urlpatterns = [
    path('create/comment/', CreateComment.as_view()),
    path('comment/<int:pk>', OneComment.as_view()),
    path('comment/<int:pk>/update', CommentUpdate.as_view()),
    path('comment/<int:pk>/delete', CommentUpdate.as_view()),

]