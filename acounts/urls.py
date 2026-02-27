from django.urls import path
from .views import RegisterView, ProfileView, ProfileImageChangeView, ProfilePasswordChangeView, RegistersView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter

# from SnippetApp import views

router = DefaultRouter()
# router.register(r)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/uploadimage/', ProfileImageChangeView.as_view(), name='profile_images'),
    path('profile/changepassword/', ProfilePasswordChangeView.as_view(), name='change_password'),
]
