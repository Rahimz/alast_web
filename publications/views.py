from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def PublicationsView(request):
    context = dict(
        page_title=_("Publications"),
        # clients=Client.objects.all().prefetch_related('solutions'),
        crumbs=[(_("Publications"), None),],
    )
    return render(
        request,
        'publications/publications.html',
        context
    )
