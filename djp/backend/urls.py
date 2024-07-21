
from django.urls import path, include
from django.http import HttpResponse,HttpResponseRedirect

urlpatterns = [
    path('', include('app.urls')),
]
