from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=150)
    rate = models.DecimalField(decimal_places=2, max_digits=5)
    is_main_skill = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-rate',)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
