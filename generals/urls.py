from django.urls import path
# from django.views.generic.base import TemplateView
from . import views

app_name = 'generals'

urlpatterns = [
    path('contact-us/', views.ContactUsView, name='contact_us'),
    path('about-us/', views.about, name='about_us'),
    path('tags/<str:tag_slug>/', views.TagListView, name='tags'),
    path('', views.HomeView, name='home'),
]
