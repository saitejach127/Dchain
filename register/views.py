from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request,pk):
    election = Election.objects.get(pk=pk)
    response = {}
    response["election"] = election
    return render(request, 'index.html',response)

def voterRegister(request):
    return render(request,'voter.html')

def candidateRegister(request):
    return render(request,'candidate.html')

def admin_validate(request):
    return render(request,'admin.html')

def createElection(request):
    if request.method == "POST":
        election = Election()
        election.name = request.POST["name"]
        election.description = request.POST["description"]
        election.save()
    return render(request,'create.html')

def currentElection(request):
    elections = Election.objects.all()
    response = {}
    response["elections"] = elections
    return render(request,'show.html',response)

def validateCandidate(request):
    return render(request,'valCand.html')

def validateVoter(request):
    return render(request,'valVoter.html')

def home(request):
    elections = Election.objects.all()
    response = {}
    response["elections"] = elections
    return render(request,'home_sam.html',response)

def end(request,pk):
    election = Election.objects.get(pk=pk)
    election.delete()
    return redirect('/adminpanel')


