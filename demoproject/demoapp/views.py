from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from demoapp.models import Homepage
from recaptcha.client.captcha import submit as verify_captcha

def homepage(request, **kwargs):
    #the object to attach the comments to
    homepage = Homepage.objects.all()[0]
    return render_to_response('homepage.html',
                              {'homepage': homepage},
                              #required for CSRF key
                              context_instance=RequestContext(request))

def templatetag(request, **kwargs):
    if request.POST:
        comment = request.POST["comment"]
        recaptcha_response_field = request.POST["recaptcha_response_field"]
        recaptcha_challenge_field = request.POST["recaptcha_challenge_field"]
        response = verify_captcha(recaptcha_challenge_field,
                                  recaptcha_response_field,
                                  settings.RECAPTCHA_PRIVATE_KEY,
                                  request.META["REMOTE_ADDR"])
        response = response.is_valid
    else:
        comment = None
        response = None

    return render_to_response('templatetag.html',
                              {"comment": comment, "response": response},
                              context_instance=RequestContext(request))
