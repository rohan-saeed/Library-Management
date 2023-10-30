from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View
from .forms import SignUpForm, LoginForm, ProfileUpdateForm


class signup(View):
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('book-list')
        return render(request, 'signup.html', {'form': form})

    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


class user_login(View):
    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('book-list')
            return render(request, 'login.html', {'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


class user_logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class profile(View):
    def post(self, request):
        user = request.user
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return render(request, 'profile.html', {'form': form})

    def get(self, request):
        user = request.user
        form = ProfileUpdateForm(instance=user)
        return render(request, 'profile.html', {'form': form})
