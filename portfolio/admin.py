from django.contrib import admin
from .models import Portfolio

# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill', 'slug', 'is_published', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
