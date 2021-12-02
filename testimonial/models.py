from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Testimonial(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    quote = models.TextField()
    role = models.CharField(max_length=250)
    image = models.ImageField(upload_to='testimonial', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
