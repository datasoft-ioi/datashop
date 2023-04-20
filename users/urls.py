
from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import UserRegristrationView, UserProfileView, UserLoginView

app_name = 'users'

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", UserRegristrationView.as_view(), name="registration"),
    path("profile/<int:pk>/", login_required(UserProfileView.as_view()), name="profile"), 
]
