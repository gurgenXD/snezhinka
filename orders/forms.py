from django import forms
from orders.models import Order


class PickUpForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):    
        super(PickUpForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
            'class': 'form-control', 'placeholder': 'Ваш E-mail', 'disabled': True, 'value': user.email}))
        self.fields['phone'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': '+7 *** *** ** **', 'id': 'ConsumerStockPhone', 'value': user.phone}))

    class Meta:
        model = Order
        fields = ('email', 'phone')


class DeliveryForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(DeliveryForm, self).__init__(*args, **kwargs)
        self.fields['full_name'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество', 'value': user.full_name}))
        self.fields['phone'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': '+7 *** *** ** **', 'id': 'ConsumerDeliveryPhone', 'value': user.phone}))
        self.fields['email'] = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
            'class': 'form-control', 'placeholder': 'Ваш E-mail', 'disabled': True, 'value': user.email}))
        self.fields['postcode'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Почтовый индекс', 'value': user.postcode}))
        self.fields['country'] = forms.CharField(required=False, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Россия', 'disabled': True, 'value': user.country}))
        self.fields['region'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Регион / Область', 'value': user.region}))
        self.fields['locality'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Город / Населённый пункт', 'value': user.locality}))
        self.fields['address'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Улица, дом, квартира / офис', 'value': user.address}))

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone', 'postcode', 'country', 'region', 'locality', 'address')
