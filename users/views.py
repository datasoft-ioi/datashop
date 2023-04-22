import random
import re
from django.db import IntegrityError
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from .models import Profile, User
from .mixins import MessageHandler

from django.contrib import auth, messages



def is_valid_uzbek_phone_number(phone_number):
    pattern = r'^\+998\d{9}$'
    return bool(re.match(pattern, phone_number))


# otp login
def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')

        if is_valid_uzbek_phone_number(phone_number):

        
            profile = Profile.objects.filter(phone_number=phone_number).first()
            if not profile:
                return HttpResponseRedirect(reverse('users:registration'))


            
            try:
                profile.otp = random.randint(1000, 9999)
                profile.save()
                print(profile)
            except ValidationError as e:
                print(e)

            message_handler = MessageHandler(phone_number, profile.otp ).send_otp_to_phone()
            
            return redirect(f'/users/otp/{profile.uid}')
        
        else:
            messages.warning(request, 'uzbek raqam kiriting!!!\n(+998)yoddan chiqmasin')

    return render(request, 'users/login.html')


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("users:login"))

def registration(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        phone_number = request.POST.get("phone_number")
        if is_valid_uzbek_phone_number(phone_number):
            try:

                user = User.objects.create(username=username)
                profile = Profile.objects.create(user=user, phone_number=phone_number)

                return HttpResponseRedirect(reverse('users:login'))
            
            except IntegrityError:
                messages.warning(request, 'Bunay username mavjud!!!')
                
        else:
            messages.warning(request, 'uzbek raqam kiriting!!!')


    return render(request, 'users/registration.html')


@login_required
def profile(request):

    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    
    context = {

        "title": "Profile",
        "form": form,
    }
    return render(request, 'users/profile.html', context)



def otp(request, uid):
    if request.method == "POST":
        otp = request.POST.get('otp')
        profile = Profile.objects.get(uid = uid)
        if otp == profile.otp:
            auth.login(request, profile.user)
            return HttpResponseRedirect(reverse('users:profile'))
        
        return redirect(f'/users/otp/{uid}')
    return render(request, 'users/otp.html')





# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Tabriklaymiz muaffokiyatli registrationdan ottingiz')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {
#         "form": form,
#     }
#     return render(request, 'users/registration.html', context)



# def login(request):

#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
            
#     else:
#         form = UserLoginForm()

#     context = {
#         "form": form,
#     }
#     return render(request, 'users/login.html', context)