from django.urls import path
from . import views

app_name = 'skill'
urlpatterns = [
    path('skills/', views.skill, name='skills'),
]
