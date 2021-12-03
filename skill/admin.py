from django.contrib import admin
from .models import Skill, Library
# Register your models here.


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'rate', 'is_main_skill', 'created_at']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
