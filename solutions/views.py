from django.shortcuts import render, get_object_or_404
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

def SolutionView(request, slug):    
    solution = get_object_or_404(Solution, slug=slug)
    context = dict(
        page_title=_("Solution"),
        solution=solution,
    )    
    return render(
        request,
        'solutions/solution.html',
        context
    )

# should be removed
def SolutionDetailsView(request):
    context = dict(
        page_title=_("Solution"),
    )
    
    return render(
        request,
        'solutions/solution_details.html',
        context
    )