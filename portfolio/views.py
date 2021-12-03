from django.shortcuts import render, get_object_or_404
from .models import Portfolio

# Create your views here.


def portfolio_list(request):
    portfolios = Portfolio.objects.filter(is_published=True)
    return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios})


def portfolio_detail(request, id, slug):
    portfolio = get_object_or_404(Portfolio, id=id, slug=slug)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio})
