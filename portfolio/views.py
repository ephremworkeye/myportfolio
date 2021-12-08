from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Portfolio
from skill.models import Skill
from account.models import Profile
from testimonial.models import Testimonial
from contact.forms import ContactForm


# Create your views here.


def portfolio_list(request):
    # portfolios = Portfolio.objects.filter(is_published=True)

    object_list = Portfolio.objects.filter(is_published=True)
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        portfolios = paginator.page(page)
    except PageNotAnInteger:
        portfolios = paginator.page(1)
    except EmptyPage:
        portfolios = paginator.page(paginator.num_pages)
    skills = Skill.objects.filter(is_main_skill=True)
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    profiles = Profile.objects.filter(user=request.user.is_superuser)
    form = ContactForm()
    return render(request, 'portfolio/portfolio_list.html', {
        'portfolios': portfolios,
        'skills': skills,
        'testimonials': testimonials,
        'form': form,
        'range': range(5),
        'profiles': profiles
    })


def portfolio_detail(request, id, slug):
    portfolio = get_object_or_404(Portfolio, id=id, slug=slug)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio})
