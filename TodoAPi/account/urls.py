from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from account.views  import RegisterAPIView, LogOutAPIView

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='login_view'), #We get access & refresh token here
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh_view'), #we get another access token

    path('register/', RegisterAPIView.as_view(), name='register_view'),
    path('logout/', LogOutAPIView.as_view(), name='logout_view'),
    
]