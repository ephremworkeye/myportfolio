from django.contrib import admin
from .models import Testimonial

# Register your models here.


@admin.register(Testimonial)
class AdminTestimonial(admin.ModelAdmin):
    list_display = ['user', 'quote', 'role', 'is_active']
