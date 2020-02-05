from django.shortcuts import render, redirect
from .models import *
from authentication.models import *
from django.http import HttpResponse
import random
import hashlib

# Create your views here.

def dashboard(request):
    response = {}
    elections = Election.objects.all()
    response["elections"] = elections
    try:
        vote = Voterid.objects.get(user=request.user)
        response["notapplied"] = False
        if vote.is_approved:
            response["app"] = True
            response["id"] = vote.voter_id
        else:
            response["app"] = False
        return render(request,'election/applyvote.djt', response)
    except:
        response["notapplied"] = True
        return render(request,'election/applyvote.djt', response)

def applyvote(request):
    vote = Voterid()
    vote.user = request.user
    vote.is_approved = False
    vote.voter_id = str(hashlib.sha256(str(random.randint(1,100)).encode()).hexdigest())
    vote.save()
    return redirect('/dashboard')

def admindashboard(request):
    response = {}
    voters = Voterid.objects.filter(is_approved=False)
    votes = []
    for vote in voters :
        profile = Userprofile.objects.get(user=vote.user)
        data = {}
        data["profile"] = profile
        data["vote"] = vote
        votes.append(data)
    response["votes"] = votes
    elections = Election.objects.all()
    response["elections"] = elections
    return render(request,'election/admindashboard.djt',response)

def acceptVoters(request):
    if request.method == "POST":
        pk = request.POST["pk"]
        vote = Voterid.objects.get(pk=pk)
        vote.is_approved = True
        vote.save()
        return redirect('/adminpanel/')
    return redirect('/adminpanel/')

def createElection(request):
    if request.method == "POST":
        election = Election()
        election.name = request.POST["name"]
        election.constituency = request.POST["constituency"]
        election.start_date = str(request.POST["start_data"])
        election.end_date = str(request.POST["end_date"])
        election.save()
        return redirect("/adminpanel")
    return redirect('/adminpanel')

def candidatepanel(request):
    elections = Election.objects.all()
    candidate = CandidateProfile.objects.get(user=request.user)
    response = {}
    response["elections"] = elections
    response["candidate"] = candidate
    return render(request,'election/candidateportal.djt',response)

def registerCandidate(request):
    if request.method == "POST":
        election = Election.objects.get(pk=request.POST["pke"])
        candidate = CandidateProfile.objects.get(pk=request.POST["pkc"])
        registration = CandidateRegistrations()
        registration.election = election
        registration.party = candidate
        registration.save()
        return redirect('/candidatepanel')
    return redirect('/candidatepanel/')

def vote(request,pke):
    election = Election.objects.get(pk=pke)
    candidates = CandidateRegistrations.objects.filter(election=election)
    response = {}
    response["election"] = election
    response["candidates"] = candidates
    return render(request, 'election/vote.djt',response)
