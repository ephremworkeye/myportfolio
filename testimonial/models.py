from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    description = models.TextField()
    role = models.CharField(max_length=250)
    image = models.ImageField(upload_to='testimonial/', blank=True, null=True)
