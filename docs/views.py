from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'docs/pages/home.html', context={
        'title': 'Home',
    })

def docs(request):
    return render(request, 'docs/pages/docs.html', context={
        'title': 'Docs',
    })

def getting_started(request):
    return render (request, 'docs/pages/getting-started.html',context={
        'title': 'Getting Started',
    })

def working_with_versacord(request):
    return render (request, 'docs/pages/working_with_versacord.html',context={
        'title': 'Working With Versacord',
    })

def a_primer_to_gateway_intents(request):
    return render (request, 'docs/pages/a_primer_to_gateway_intents.html',context={
        'title': 'A Primer to Gateway Intents',
    })

def migration(request):
    return render (request, 'docs/pages/migration.html',context={
        'title': 'Migrating to versacord',
    })

def help(request):
    return render (request, 'docs/pages/help.html',context={
        'title': 'Getting help',
    })

def faqs(request):
    return render (request, 'docs/pages/faqs.html',context={
        'title': 'FAQs',
    })

def extensions(request):
    return render (request, 'docs/pages/extensions.html',context={
        'title': 'Extensions',
    })

def manuals(request):
    return render (request, 'docs/pages/manuals.html',context={
        'title': 'Manuals',
    })

def meta(request):
    return render (request, 'docs/pages/meta.html',context={
        'title': 'Meta',
    })