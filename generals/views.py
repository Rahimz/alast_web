from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.models import TeamMember
from solutions.models import Solution, Award
from multimedias.models import Gallery
from .forms import ContactForm


def HomeView(request):
    solutions = Solution.objects.all().order_by('?')[:4]
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
        solutions=Solution.objects.order_by('?')[:4],
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