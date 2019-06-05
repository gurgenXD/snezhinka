from django import forms
from feedback.models import CallBack, FeedBack


class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = ('phone',)
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "+7 *** *** ** **", 'id': "CallBackModalPhone"}),
        }


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('email', 'name', 'message')
        widgets = {
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': "E-mail"}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше имя"}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Сообщение...", 'rows': 5}),   
        }