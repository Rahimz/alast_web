from django.urls import path
from . import views 

app_name = 'solutions'

urlpatterns = [
    path('', views.SolutionsView, name='solutions'),
    path('details/', views.SolutionView, name='solution_details'),
]

