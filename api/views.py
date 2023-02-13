from django.http import HttpResponse
from django.shortcuts import render


def api(request):
    return render(request, 'api/pages/api.html', context={
        'title': 'API Reference',
    })
