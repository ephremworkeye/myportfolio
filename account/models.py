from django.db import models
from django.contrib.auth.models import User
from skill.models import Skill

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name='user_skills')
    linkden_url = models.URLField(max_length=250, blank=True)
    website_url = models.URLField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='profile', blank=True, null=True)
    title = models.CharField(max_length=250)
    resume = models.FileField(upload_to='resume', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
