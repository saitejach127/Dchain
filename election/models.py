from django.db import models
from django.contrib.auth.models import User
from authentication.models import *

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.party.party_name, filename)

class Voterid(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    voter_id = models.CharField(default="", max_length=100)

    def __str__(self):
        return self.user.username

class Election(models.Model):
    name = models.CharField(max_length=200)
    constituency = models.CharField(max_length=100)
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CandidateRegistrations(models.Model):
    election = models.ForeignKey(Election,on_delete=models.CASCADE)
    party = models.ForeignKey(CandidateProfile,on_delete=models.CASCADE)
    manifesto = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.party.party_name

class Votes(models.Model):
    election = models.ForeignKey(Election,on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateProfile,on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return self.candidate.party_name

class Tokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return self.user.username

class Proofread(models.Model):
    election = models.ForeignKey(Election,on_delete=models.CASCADE)
    manifesto = models.ForeignKey(CandidateRegistrations,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    comments = models.TextField(default="")

    def __str__(self):
        return self.manifesto.party.party_name




