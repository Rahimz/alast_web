from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .models import Solution

def SolutionsView(request):
    solutions = Solution.objects.all()
    context = dict(
        page_title=_("Solutios"),
        solutions=solutions
    )
    
    return render(
        request,
        'solutions/solutions.html',
        context
    )

def SolutionView(request):
    context = dict(
        page_title=_("Solutio"),
    )
    
    return render(
        request,
        'solutions/solution.html',
        context
    )