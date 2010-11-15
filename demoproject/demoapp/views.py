from django.shortcuts import render_to_response
from demoapp.models import Homepage
from django.template import RequestContext

def homepage(request, **kwargs):
    homepage = Homepage.objects.all()[0]
    return render_to_response('homepage.html',
                              {'homepage': homepage},
                              context_instance=RequestContext(request))
