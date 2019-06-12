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