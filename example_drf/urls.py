from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('account_app.urls')),
    path('', include('post_app.urls')),
    path('', include('comment_app.urls')),
]
