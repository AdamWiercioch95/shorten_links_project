from django import forms

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from shorten_links_app.models import Link


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz Hasło', widget=forms.PasswordInput)
    email = forms.EmailField(label='Adres email')

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('Hasła muszą być takie same')
        return cd['password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Użytkownik o takim loginie już istnieje')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ten email jest już używany')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError('Niepoprawne dane logowania')
        except User.DoesNotExist:
            raise forms.ValidationError('Niepoprawne dane logowania')

        return cleaned_data


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['original_url']
        labels = {'original_url': 'Link do skrócenia'}
        widgets = {
            'original_url': forms.URLInput(attrs={'placeholder': 'Wprowadź link do skrócenia'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(LinkForm, self).__init__(*args, **kwargs)

    def clean_original_url(self):
        original_url = self.cleaned_data.get('original_url')

        if self.user and Link.objects.filter(original_url=original_url, user=self.user).exists():
            raise ValidationError('Podany link już jest skrócony.')

        return original_url
