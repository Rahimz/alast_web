from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from accounts.models import TeamMember

def about(request):
    context = dict(
        page_title=_("About us"),
        crumbs=[(_("About us"), None),],
        team_members = TeamMember.objects.all().order_by('rank')
    )
    return render(
        request,
        'generals/about_us.html',
        context

    )