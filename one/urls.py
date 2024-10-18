from django.urls import path
from . import views  # تأكد من استيراد views بشكل صحيح

urlpatterns = [
    path('', views.home, name='home'),  # تأكد من أن home معرف في views
]
