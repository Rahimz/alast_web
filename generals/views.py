from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from accounts.models import TeamMember
from solutions.models import Solution, Award

def about(request):
    context = dict(
        page_title=_("About us"),
        crumbs=[(_("About us"), None),],
        team_members = TeamMember.objects.all().order_by('rank'),
        solutions=Solution.objects.order_by('?')[:4],
        awards=Award.objects.all()
    )
    return render(
        request,
        'generals/about_us.html',
        context

    )