from django.urls import path
from election import views

urlpatterns = [
    path('dashboard/',views.dashboard),
    path('adminpanel/', views.admindashboard),
    path('acceptvote/', views.acceptVoters),
    path('applyvote/', views.applyvote),
    path('createElection/', views.createElection),
    path('candidatepanel/', views.candidatepanel),
    path('registerCandidate/', views.registerCandidate),
    path('vote/<int:pke>', views.vote),
    path('castVote/', views.castVote),
    path('results/<int:pke>', views.results),
    path('survey/<int:pke>', views.survey),
    path('surveysubmit/',views.storeResponse),
]
