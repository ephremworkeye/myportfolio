from django.db import models
from django.contrib.auth.models import User
from skill.models import Skill

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to='portfolios/', blank=True)
    is_published = models.BooleanField(default=True, null=True)
    description = models.TextField(blank=True)
    website_link = models.URLField(max_length=250, blank=True)
    github_link = models.URLField(max_length=350, blank=True)
    skill = models.ManyToManyField(
        'Skill', through='PortfolioSkill', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
