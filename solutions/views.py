from django.shortcuts import render
from django.utils.translation import gettext_lazy as _



def SolutionsView(request):
    context = dict(
        page_title=_("Solutios"),
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