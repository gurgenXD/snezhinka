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
    def __init__(self, user, *args, **kwargs):
        super(FeedBackForm, self).__init__(*args, **kwargs)
        if user.is_anonymous:
            self.fields['name'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ваше имя'}))
            self.fields['email'] = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'E-mail'}))
        else:
            self.fields['name'] = forms.CharField(required=True, widget=forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ваше имя', 'value': user.full_name}))
            self.fields['email'] = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'E-mail', 'value': user.email}))

    class Meta:
        model = FeedBack
        fields = ('email', 'name', 'message')
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Сообщение...", 'rows': 5}),   
        }