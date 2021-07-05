from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account_app.views import UserRegistrationAPIView, LogoutView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('logout/', LogoutView.as_view(), name='auth_logout'),
]