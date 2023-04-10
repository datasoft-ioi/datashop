from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

from django.contrib import auth, messages
from django.contrib.messages.views import SuccessMessageMixin


def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
            
    else:
        form = UserLoginForm()

    context = {
        "form": form,
    }
    return render(request, 'users/login.html', context)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegristrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = "Tabriklaymiz muaffokiyatli registrationdan ottingiz"

    def get_context_data(self, **kwargs):
        context = super(UserRegristrationView, self).get_context_data()
        context['title'] = "Datashop - User Registrations"
        return context


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'


    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = "Datashop - User Profile"
        # context['basket'] = Basket.objects.filter(user=self.object)
        return context




# @login_required
# def profile(request):

#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
    
#     context = {

#         "title": "Profile",
#         "form": form,
#     }
#     return render(request, 'users/profile.html', context)


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