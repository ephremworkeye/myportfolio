from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from .models import Portfolio
from skill.models import Skill, Library
from account.models import Profile
from testimonial.models import Testimonial
from contact.forms import ContactForm
from comment.forms import PortfolioCommentForm
from comment.models import Comment


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
    technologies = Library.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {
        'portfolios': portfolios,
        'skills': skills,
        'testimonials': testimonials,
        'form': form,
        'range': range(5),
        'profiles': profiles,
        'technologies': technologies,
    })


def portfolio_detail(request, id, slug):
    portfolio = get_object_or_404(Portfolio, id=id, slug=slug)

    comments = portfolio.comments.filter(is_active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = PortfolioCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.portfolio = portfolio
            new_comment.save()
    else:
        comment_form = PortfolioCommentForm()

    return render(request, 'portfolio/portfolio_detail.html', {
        'portfolio': portfolio,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment})


def portfolio_search(request):
    query = request.GET.get('query', '')
    results = Portfolio.objects.annotate(
        search=SearchVector('name', 'description'),).filter(search=query)
    if query:
        return render(request, 'portfolio/search.html', {'query': query, 'results': results})
    else:
        return render(request, 'portfolio/portfolio_list.html')


def port_page(request):
    object_list = Portfolio.objects.filter(is_published=True)
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        portfolios = paginator.page(page)
    except PageNotAnInteger:
        portfolios = paginator.page(1)
    except EmptyPage:
        portfolios = paginator.page(paginator.num_pages)

    return render(request, 'portfolio/port_pages.html', {'portfolios': portfolios})


def about(request):
    return render(request, 'portfolio/about.html')
