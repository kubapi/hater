from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'feed/index.html', {})

def contact(request):
    return render(request, 'feed/contact.html', {})

def about(request):
    return render(request, 'feed/about.html', {})