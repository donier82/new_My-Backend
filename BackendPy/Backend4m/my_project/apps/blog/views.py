from django.shortcuts import render

# Create your views here.

def index(request):
    title={'open':'probniy text'}
    return render(request, 'index.html', title)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')