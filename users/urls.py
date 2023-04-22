
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("otp/<uid>/", views.otp, name="otp"),
]