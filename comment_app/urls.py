from django.urls import path

from comment_app.views import CreateComment, CommentUpdate, OneCommentDetail


urlpatterns = [
    path('create/comment/', CreateComment.as_view()),
    path('comment/<int:pk>/update', CommentUpdate.as_view()),
    path('comment/<int:pk>', OneCommentDetail.as_view()),
]