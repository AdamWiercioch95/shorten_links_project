from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from shorten_links_app.forms import RegisterForm


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
