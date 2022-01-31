from django.shortcuts import render
from .models import Skill

# Create your views here.


def skill(request):
    skills = Skill.objects.filter(is_main_skill=True)
    return render(request, 'skill/skills.html', {'skills': skills})
