from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'ext/pages/home.html', context={
        'title': 'Home',
    })

def commands(request):
    return render(request, 'ext/pages/commands.html', context={
        'title': 'Ext Commands',
    })

def tasks(request):
    return render(request, 'ext/pages/tasks.html', context={
        'title': 'Taks Commands',
    })

def application_checks(request):
    return render(request, 'ext/pages/application_checks.html', context={
        'title': 'Application Checks',
    })


