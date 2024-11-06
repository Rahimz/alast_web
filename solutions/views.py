from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch, Count, Q

from .models import Solution, SolutionCategory

def SolutionsView(request):
    solutions = Solution.actives.all()
    
    categories = SolutionCategory.objects.annotate(
    active_solution_count=Count('solutions', filter=Q(solutions__in=solutions))
        ).filter(active_solution_count__gt=0).prefetch_related(Prefetch('solutions', queryset=solutions))
    context = dict(
        page_title=_("Solutios"),
        # solutions=solutions,
        categories=categories,
        crumbs=[(_("Solutions"), None)]
    )
    
    return render(
        request,
        'solutions/solutions.html',
        context
    )

def SolutionView(request, slug):    
    solution = get_object_or_404(Solution, slug=slug, active=True)
    context = dict(
        page_title=_("Solution"),
        solution=solution,
        crumbs=[
            (_("Solutions"), 'solutions:solutions'),
            (solution.title, None),
            ]
    )    
    return render(
        request,
        'solutions/solution.html',
        context
    )

# should be removed
# def SolutionDetailsView(request):
#     context = dict(
#         page_title=_("Solution"),
#     )
    
#     return render(
#         request,
#         'solutions/solution_details.html',
#         context
#     )