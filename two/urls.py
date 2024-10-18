from django.urls import path
from . import views

urlpatterns = [
    path('two/', views.about, name='about'),
    path('', views.about, name='about'),
]
