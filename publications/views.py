from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .models import Publication


def PublicationsView(request):
    context = dict(
        page_title=_("Publications"),
        pubs=Publication.objects.all(),
        crumbs=[(_("Publications"), None),],
    )
    return render(
        request,
        'publications/publications.html',
        context
    )
