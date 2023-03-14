
from django.shortcuts import render,redirect,get_object_or_404
from .forms import  ClientRegistrationForm


from .models import Client
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


#@login_required
@user_passes_test(lambda u: u.groups.filter(name='Account Manager').exists(), login_url='home')
def client_register(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = ClientRegistrationForm()
    return render(request, 'register_client.html', {'form': form})


@login_required

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the admin dashboard
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')




def home(request):
    return render(request, 'dashboard.html')



@login_required
@user_passes_test(lambda u: u.groups.filter(name='Account Manager').exists(), login_url='home')

def dashboard(request):
    return render(request, 'dashboard.html')




@login_required
@user_passes_test(lambda u: u.groups.filter(name='Account Manager').exists(), login_url='home')
def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST, instance=client)
        if form.is_valid():
            user = form.save()
            return redirect('edit_client')
    else:
        form = ClientRegistrationForm(instance=client)
    return render(request, 'edit_client.html', {'form': form, 'client': client})




@user_passes_test(lambda u: u.groups.filter(name='Account Manager').exists(), login_url='home')
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('view_clients')
    return render(request, 'delete_client.html', {'client': client})




@user_passes_test(lambda u: u.groups.filter(name='Account Manager').exists(), login_url='home')
def view_clients(request):
    group = Group.objects.get(name='Client')
    clients = group.user_set.all()

    context = {
        'clients': clients,
    }
    return render(request, 'view_clients.html', context)


@receiver(post_save, sender=User)
def set_user_permissions(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Client')
        instance.groups.add(group)







@login_required
def client_dashboard(request):
    user = request.user
    return render(request, 'client_dashboard.html', {'user': user})

def client_login(request):
    if request.method == 'POST':
        # Get the username and password from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user against the client authentication system
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user and redirect to the home page
            login(request, user)
            return redirect('client_dashboard')
        else:
            # Return an error message if authentication fails
            error_message = "Invalid username or password"
            return render(request, 'client_login.html', {'error_message': error_message})

    # Render the client login page for GET requests
    return render(request, 'client_login.html')



def user_logout(request):
    logout(request)
    return redirect('login')

def client_logout(request):
    logout(request)
    return redirect('client_login')