from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'feed/index.html', {})

def contact(request):
    return render(request, 'feed/contact.html', {})

def about(request):
    return render(request, 'feed/about.html', {})

def ranking(request):
    return render(request, 'feed/ranking.html', {})

def architect(request):
    return render(request, 'feed/architect.html', {})