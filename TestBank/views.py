from django.views.generic import ListView
from django.shortcuts import render,redirect,get_object_or_404

from TestBank.forms import CustomUserCreationForm
from .forms import CustomUserCreationForm, UserAddressForm, UserRegistrationForm

from .models import Client
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client, UserAddress



@login_required
def home(request):
    return redirect('register_client')


@login_required

def register_client(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        address_form = UserAddressForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data['email']
            user.save()
            address = address_form.save(commit=False)
            address.user = user
            address.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        address_form = UserAddressForm()
    return render(request, 'register_client.html', {
        'user_form': user_form,
        'address_form': address_form
    })

group_name = 'Client'
new_group, created = Group.objects.get_or_create(name=group_name)



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
        form = form(request.POST, instance=client)
        if form.is_valid():
            form.save()
    else:
        form = form(instance=client)
    return render(request, 'edit_client.html', {'form': form, 'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect('view_clients')


@receiver(post_save, sender=User)
def set_user_permissions(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Client')
        instance.groups.add(group)



@login_required
def client_dashboard(request):
    try:
        client = Client.objects.get(user=request.user)
    except Client.DoesNotExist:
        client = None

    context = {
        'client': client
    }
    return render(request, 'client_dashboard.html', context)

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