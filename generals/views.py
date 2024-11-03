from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch, Count, Q
from taggit.models import Tag

from accounts.models import TeamMember
from solutions.models import Solution, Award, SolutionCategory
from multimedias.models import Gallery
from .forms import ContactForm


def HomeView(request):
    solutions = Solution.actives.all().order_by('?')[:2]
    context = dict(
        page_title=_("Home"),
        solutions=solutions,
        team_members = TeamMember.objects.all().order_by('rank'),
        awards=Award.objects.all(),
    )
    return render(
        request,
        'generals/home.html',
        context
    )


def about(request):
    context = dict(
        page_title=_("About us"),
        crumbs=[(_("About us"), None),],
        team_members = TeamMember.objects.all().order_by('rank'),
        solutions=Solution.actives.all().order_by('?')[:4],
        awards=Award.objects.all(),
        galleries=Gallery.objects.all()
    )
    return render(
        request,
        'generals/about_us.html',
        context

    )


def ContactUsView(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('generals:contact_us')}#logo")
    else:
        form = ContactForm()
    context = dict(
        page_title=_("Contact us"),
        form=form,
    )
    return render (
        request,
        'generals/contact_us.html',
        context
    )    
    
    
def TagListView(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    solutions = Solution.actives.filter(tags__in=[tag])    
    
    categories = SolutionCategory.objects.annotate(
    active_solution_count=Count('solutions', filter=Q(solutions__in=solutions))
        ).filter(active_solution_count__gt=0).prefetch_related(Prefetch('solutions', queryset=solutions))
    context = dict(
        page_title=_("Tag") + f": {tag.name}",
        # search_query=search_query,
        categories=categories,
        tag=tag,

    )
    return render(
        request,
        'solutions/solutions.html',
        context
    )