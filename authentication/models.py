from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.party_name, filename)

class Userprofile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    aadhar_number = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username

class CandidateProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party_name = models.CharField(max_length=200)
    party_short = models.CharField(max_length=10)
    party_symbol = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.user.username
