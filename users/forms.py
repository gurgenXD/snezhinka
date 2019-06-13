from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class LoginForm(forms.ModelForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'customCheck1'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'remember_me')
        widgets = {
            'username': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'E-mail'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
        }
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError('E-mail или пароль неверный')
                print('я тут')
        except User.DoesNotExist:
            raise forms.ValidationError('E-mail или пароль неверный')
            print('а я тут')


class RegisterForm(UserCreationForm):
    username = forms.EmailField(required=True, widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'E-mail'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с такой почтой уже существует')

        return username    
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')

        return password2



class UserInfoForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields['full_name'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество', 'value': user.full_name}))
        self.fields['phone'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': '+7 *** *** ** **', 'id': 'ConsumerProfilePhone', 'value': user.phone}))
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
        model = User
        fields = ('phone', 'full_name', 'postcode', 'country', 'region', 'locality', 'address')