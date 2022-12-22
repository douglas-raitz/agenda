from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def register(request):
    
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio!')
        return render(request, 'accounts/register.html')
            
    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')    
