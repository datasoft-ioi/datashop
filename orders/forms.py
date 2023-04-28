from django import forms

from orders.models import Order


# class OrderForm(forms.ModelForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control', 'placeholder': 'Россия, Москва, ул. Мира, дом 6',
#     }))

#     class Meta:
#         model = Order
#         fields = ('first_name', 'last_name', 'email', 'address', 'initiator')

        

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_method', 'region', 'city', 'address', 'payment_method', 'first_name', 'last_name', 'phone_number', 'additional_phone_number']
        labels = {
            'delivery_method': 'Как вы хотите получить заказ?',
            'region': 'Область',
            'city': 'Город',
            'address': 'Полный адрес',
            'payment_method': 'Выберите способ оплаты',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone_number': 'Телефон',
            'additional_phone_number': 'Дополнительный телефон',
        }
        widgets = {
            'delivery_method': forms.RadioSelect(),
            'payment_method': forms.RadioSelect(),
        }