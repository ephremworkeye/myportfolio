from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from skill.models import Skill, Library

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=150)
    skill = models.ManyToManyField(Skill)
    library = models.ManyToManyField(Library, blank=True)
    slug = models.SlugField(max_length=150)
    model_design_url = models.URLField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='portfolios', blank=True)
    is_published = models.BooleanField(default=True, null=True)
    description = models.TextField(blank=True)
    website_link = models.URLField(max_length=250, blank=True)
    github_link = models.URLField(max_length=350, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
