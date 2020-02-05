from django.urls import path
from authentication import views

urlpatterns = [
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('profile/', views.party_register),
]
