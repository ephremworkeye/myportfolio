from django.shortcuts import render

# Create your views here.


def portfolio_list(request):
    return render(request, 'portfolio/portfolio_list.html')


def portfolio_detail(request):
    return render(request, 'portfolio/portfolio_detail.html')
