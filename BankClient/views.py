from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'user/login.html', context)

def user_dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'user/dashboard.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_login')