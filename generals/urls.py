from django.urls import path
from django.views.generic.base import TemplateView


app_name = 'generals'

urlpatterns = [
    path('', TemplateView.as_view(template_name='generals/home.html'), {'page_title': 'Home'}, name='home'),
    path('solutions/', TemplateView.as_view(template_name='generals/solutions.html'), {'page_title': 'Solutions'}, name='solutions'),
    path('publications/', TemplateView.as_view(template_name='generals/publications.html'), {'page_title': 'Publications'}, name='publications'),
    path('clients/', TemplateView.as_view(template_name='generals/clients.html'), {'page_title': 'Clients'}, name='clients'),
    path('contact-us/', TemplateView.as_view(template_name='generals/contact_us.html'), {'page_title': 'Contact us'}, name='contact_us'),
    path('about-us/', TemplateView.as_view(template_name='generals/about_us.html'), {'page_title': 'About us'}, name='about_us'),
]
