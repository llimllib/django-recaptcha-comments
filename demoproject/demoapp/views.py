from django.shortcuts import render_to_response
from demoapp.models import Homepage
from django.template import RequestContext

def homepage(request, **kwargs):
    #the object to attach the comments to
    homepage = Homepage.objects.all()[0]
    return render_to_response('homepage.html',
                              {'homepage': homepage},
                              #required for CSRF key
                              context_instance=RequestContext(request))

def templatetag(request, **kwargs):
    return render_to_response('templatetag.html',
                              context_instance=RequestContext(request))
