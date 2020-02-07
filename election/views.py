from django.shortcuts import render, redirect
from .models import *
from authentication.models import *
from django.http import HttpResponse
import random
import hashlib

from django.core.mail import send_mail

# Create your views here.

def dashboard(request):
    response = {}
    elections = Election.objects.all()
    final_elections = []
    for ele in elections:
        data = {}
        data["yes"] = random.randint(0,1)
        data["election"] = ele
        final_elections.append(data)
    response["elections"] = final_elections
    try:
        tokens = Tokens.objects.get(user=request.user)
        response["tokens"] = tokens
    except:
        pass
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
    final_cand = []
    for cand in candidates:
        data = {}
        try:
            data["score"] = Proofread.objects.get(election=election,manifesto=cand)
        except:
            data["score"] = 0
        data["data"] = cand
        final_cand.append(data)
    response = {}
    response["election"] = election
    response["candidates"] = final_cand
    return render(request, 'election/vote.djt',response)

def castVote(request):
    if request.method == "POST":
        election = Election.objects.get(pk=request.POST["pke"])
        profile = CandidateProfile.objects.get(pk=request.POST["pkc"])
        try:
            vote = Votes.objects.get(election=election, candidate=profile)
            vote.count+=1
            vote.save()
        except:
            vote = Votes()
            vote.election = election
            vote.candidate = profile
            vote.count = 1
            vote.save()
        token = Tokens.objects.get(user=request.user)
        token.count+=1
        token.save()
        Content = 'Your Vote has been casted to ' + profile.party_name +'\n\n'
        Content+= 'Thank you for using Dchain'
        
        receiver = request.user.email
        sender = "chsaiteja@student.nitw.ac.in"
        rlist = []
        rlist.append(receiver)
        try:
            send_mail('Dchain Voting message ',Content,sender,rlist,fail_silently=False,)
            return redirect('/')
        except :
            pass
        return redirect('/')
    return redirect('/')

def results(request,pke):
    votes = Votes.objects.filter(election=Election.objects.get(pk=pke))
    response = {}
    response["votes"] = votes
    return render(request, 'election/results.djt',response)

def survey(request,pke):
    reg = CandidateRegistrations.objects.filter(election=Election.objects.get(pk=pke))
    response = {}
    response["regs"] = reg
    return render(request,'election/survey.djt',response)

def storeResponse(request):
    if request.method == "POST":
        cand = CandidateRegistrations.objects.get(pk=request.POST["pkc"])
        ele = Election.objects.get(pk=request.POST["pke"])
        try:
            proof = Proofread.objects.get(manifesto=cand,election=ele)
            proof.score+=int(request.POST["score"])
            proof.comments+="\n\n"
            proof.comments+=request.POST["comment"]
            proof.save()
        except:
            proof = Proofread()
            proof.manifesto = cand
            proof.election = ele
            proof.score = int(request.POST["score"])
            proof.comments = request.POST["comment"]
            proof.save()
    return redirect('/dashboard')


