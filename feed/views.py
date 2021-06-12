from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    # Choose random deck try until finds one that fits
    if Deck.objects.filter(pk=1).exists():
        for i in range(Deck.objects.all().count()):
            deck = Deck.objects.order_by('?')[0]
            if len(deck.get_cards()):
                cards = deck.get_cards()
                return render(request, 'feed/index.html', {'cards' : cards})
    return render(request, 'feed/index.html', {})

def contact(request):
    return render(request, 'feed/contact.html', {})

def about(request):
    return render(request, 'feed/about.html', {})

def ranking(request):
    # Checks if there is at least one record
    if User.objects.filter(pk=1).exists():
        users_scores = User.objects.order_by('-score')
        return render(request, 'feed/ranking.html', {'users_scores' : users_scores})
    return render(request, 'feed/index.html', {})

def architect(request):
    return render(request, 'feed/architect.html', {})