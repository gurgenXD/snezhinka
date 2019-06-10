from django import forms
from orders.models import Order


class PickUpForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):    
        super(PickUpForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Ваш E-mail', 'value': user.email}))
        self.fields['phone'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': '+7 *** *** ** **', 'id': 'ConsumerDeliveryPhone', 'value': user.username}))

    class Meta:
        model = Order
        fields = ('email', 'phone')
        # widgets = {
        #     'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш E-mail', 'value': user.username}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 *** *** ** **', 'id': 'CallBackModalPhone'}),
        # }


class DeliveryForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(DeliveryForm, self).__init__(*args, **kwargs)
        self.fields['full_name'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество', 'value': user.username}))
        self.fields['phone'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': '+7 *** *** ** **', 'id': 'ConsumerDeliveryPhone', 'value': user.username}))
        self.fields['email'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Ваш E-mail', 'value': user.email}))
        self.fields['postcode'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Почтовый индекс', 'value': user.username}))
        self.fields['country'] = forms.CharField(required=False, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Россия', 'disabled': True, 'value': user.username}))
        self.fields['region'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Регион / Область', 'value': user.username}))
        self.fields['locality'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Город / Населённый пункт', 'value': user.username}))
        self.fields['address'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Улица, дом, квартира / офис', 'value': user.username}))

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone', 'postcode', 'country', 'region', 'locality', 'address')
        # widgets = {
        #     'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш E-mail'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 *** *** ** **', 'id': 'ConsumerDeliveryPhone'}),
        #     'postcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Почтовый индекс'}),
        #     'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Россия', 'disabled': True}),
        #     'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Регион / Область'}),
        #     'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Город / Населённый пункт'}),
        #     'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Улица, дом, квартира / офис'}),
        # }