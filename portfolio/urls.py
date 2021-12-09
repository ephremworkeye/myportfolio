from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('search/', views.portfolio_search, name='search'),
    path('<int:id>/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
]
