from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('download/', views.download_resume, name='download'),
]
