from django.urls import path

from docs.views import (a_primer_to_gateway_intents, docs, faqs,
                        getting_started, help, home, migration,
                        working_with_versacord, extensions, manuals, meta)

urlpatterns = [
    path('', home ),
    path('docs/', docs),
    path('docs/gettingstarted/', getting_started),
    path('docs/workingwithversacord/', working_with_versacord),
    path('docs/aprimertogatewayintents/', a_primer_to_gateway_intents),
    path('docs/migration/', migration),
    path('docs/help/', help),
    path('docs/faqs/', faqs),
    path('docs/extensions/', extensions),
    path('docs/manuals/', manuals),
    path('docs/meta/', meta),
]
