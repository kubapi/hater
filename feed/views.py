from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import *
from .forms import *

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Zalogowano. Witaj {username}.')
                return redirect('feed:index')
            else:
                messages.error(request,'Błędny login lub hasło.')
        else:
            messages.error(request,'Błędny login lub hasło.')
    form = AuthenticationForm()
    return render(request,'feed/login.html', {'login_form' : form})

def register_view(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Rejestracja zakończona pomyślnie.')
			return redirect('feed:index')
		messages.error(request, 'Nieudana rejestracja. Błędne dane.')
	form = NewUserForm
	return render (request, 'feed/register.html', {"register_form" : form})

def logout_view(request):
	logout(request)
	messages.info(request, "Wylogowywanie zakończone pomyślnie!") 
	return redirect("feed:index")

def contact(request):
    return render(request, 'feed/contact.html', {})

def about(request):
    return render(request, 'feed/about.html', {})

def ranking(request):
    # Checks if there is at least one record
    if Player.objects.filter(pk=1).exists():
        users_scores = Player.objects.order_by('-score')
        return render(request, 'feed/ranking.html', {'users_scores' : users_scores})
    return render(request, 'feed/index.html', {})

@login_required
def index(request):
    if Deck.objects.all():
        deck = Deck.objects.order_by('?')[0]
        cards = deck.get_cards()
        return render(request, 'feed/index.html', {'cards' : cards})
    return render(request, 'feed/index.html', {})

@login_required
def architect(request):
    return render(request, 'feed/architect.html', {})