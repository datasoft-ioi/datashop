import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.timezone import now


from users.models import User, EmailVerification

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ism kiriting'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Parol kiriting'}))
    
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ism kiriting'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Familiyani kiriting'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'telefon kiriting'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'email kiriting'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'parol kiriting'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'parolni tastiqlang'}))

    class Meta:
        model = User
        fields = ('username', 'last_name', 'phone','email', 'password1', 'password2')
    

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user

class UserProfileForm(UserChangeForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Telefon raqam'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ismingizni kiriting'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Familiyangiz'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'email'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'placeholder': 'image'}), required=False)


    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name', 'username', 'email', 'image')


