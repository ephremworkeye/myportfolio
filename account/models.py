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
