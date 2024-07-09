from django.urls import path
from . import views 

app_name = 'solutions'

urlpatterns = [
    path('', views.SolutionsView, name='solutions'),
    path('/details/', views.SolutionDetailsView, name='solution_details'), #should be removed
    path('/<str:slug>/', views.SolutionView, name='solution'),
]

