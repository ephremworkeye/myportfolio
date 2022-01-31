from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('about/', views.about, name='about'),
    path('port_pages/', views.port_page, name='port_page'),
    path('search/', views.portfolio_search, name='search'),
    path('<int:id>/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
]
