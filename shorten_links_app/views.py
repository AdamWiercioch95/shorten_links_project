from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from shorten_links_app.forms import RegisterForm, LoginForm


class LandingPageView(TemplateView):
    template_name = 'landing_page.html'


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'Rejestracja',
            'button_title': 'Zarejestruj',
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('/')
        else:
            context = {
                'form': form,
                'title': 'Rejestracja',
                'button_title': 'Zarejestruj',
            }
            return render(request, 'form.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
            'title': 'Logowanie',
            'button_title': 'Zaloguj',
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            login(request, user)
            return redirect('/')

        context = {
            'form': form,
            'title': 'Logowanie',
            'button_title': 'Zaloguj',
        }
        return render(request, 'form.html', context)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('landing_page')

