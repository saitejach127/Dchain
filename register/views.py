from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def voterRegister(request):
    return render(request,'voter.html')

def candidateRegister(request):
    return render(request,'candidate.html')
