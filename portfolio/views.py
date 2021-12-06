from django.shortcuts import render, get_object_or_404
from .models import Portfolio
from skill.models import Skill
from testimonial.models import Testimonial
from contact.forms import ContactForm


# Create your views here.


def portfolio_list(request):
    portfolios = Portfolio.objects.filter(is_published=True)
    skills = Skill.objects.filter(is_main_skill=True)
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    form = ContactForm()
    return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios, 'skills': skills, 'testimonials': testimonials, 'form': form, 'range': range(5)})


def portfolio_detail(request, id, slug):
    portfolio = get_object_or_404(Portfolio, id=id, slug=slug)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio})
