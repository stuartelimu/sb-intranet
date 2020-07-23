from django.urls import path, include
from .views import RegistrationView, ProfileView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
