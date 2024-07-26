from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .models import Client


def ClientListView(request):
    context = dict(
        page_title=_("Clients"),
        clients=Client.objects.all().prefetch_related('solutions'),
        crumbs=[(_("Clients"), None),],
    )
    return render(
        request,
        'clients/clients.html',
        context
    )
