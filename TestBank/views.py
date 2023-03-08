from django.views.generic import ListView
from django.shortcuts import render,redirect,get_object_or_404
from .forms import ClientForm
from .models import Client
from django.contrib.auth import authenticate, login as auth_login,logout

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return redirect('register_client')


@login_required

def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.active = True
            client.save()
            return redirect('view_clients')#or add register_client.html to clear the form 
    else:
        form = ClientForm()

    context = {'form': form}
    return render(request, 'register_client.html', context)

@login_required

def view_clients(request):
    clients = Client.objects.all()
    return render(request, 'view_clients.html', {'clients': clients})


##create new user
#from django.contrib.auth.models import User
#>>> User.objects.create_user('test', 'test@test.com', '1234')




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

def home(request):
    return render(request, 'view_clients.html')




def dashboard(request):
    return render(request, 'dashboard.html')






def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form, 'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect('view_clients')
