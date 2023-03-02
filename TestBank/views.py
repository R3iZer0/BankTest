from django.shortcuts import render,redirect    
from .forms import ClientForm
from .models import Client

def home(request):
    return redirect('register_client')




def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page
    else:
        form = ClientForm()
    return render(request, 'register_client.html', {'form': form})

def view_clients(request):
    clients = Client.objects.all()
    return render(request, 'view_clients.html', {'clients': clients})