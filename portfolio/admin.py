from django.contrib import admin
from .models import Portfolio

# Register your models here.


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_published', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
