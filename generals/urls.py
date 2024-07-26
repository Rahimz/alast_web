from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'generals'

urlpatterns = [
    path('', TemplateView.as_view(template_name='generals/home.html'), {'page_title': 'Home'}, name='home'),
    path('contact-us/', TemplateView.as_view(template_name='generals/contact_us.html'), {'page_title': 'Contact us'}, name='contact_us'),
    path('about-us/', views.about, name='about_us'),
]
