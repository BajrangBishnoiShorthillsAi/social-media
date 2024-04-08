from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('profile/', views.user_profile),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenObtainPairView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenObtainPairView.as_view(), name='token_verify'),
]
