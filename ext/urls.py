from django.urls import path

from ext.views import application_checks, commands, home, tasks

urlpatterns = [
    path('', home ),
    path('ext/commands/', commands),
    path('ext/tasks/', tasks),
    path('ext/application_checks/', application_checks),
]