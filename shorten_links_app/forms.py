from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz Hasło', widget=forms.PasswordInput)
    email = forms.EmailField(label='Adres email')

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def check_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('Hasła muszą być takie same')
        return cd['password2']

    def check_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Użytkownik o takim loginie już istnieje')
        return username

    def check_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ten email jest już używany')
        return email


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
