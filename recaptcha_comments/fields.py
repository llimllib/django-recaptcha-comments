from django.conf import settings
from django import forms
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

#We use the [recaptcha-client](http://pypi.python.org/pypi/recaptcha-client) to handle our recaptcha code
from recaptcha.client import captcha

from recaptcha_comments.widgets import ReCaptcha

captcha.API_SERVER="http://www.google.com/recaptcha/api"
captcha.VERIFY_SERVER="www.google.com/recaptcha/api"

#the code in this class is derived from [Marco Fucci's very useful snippets](http://www.marcofucci.com/tumblelog/26/jul/2009/integrating-recaptcha-with-django/)
class ReCaptchaField(forms.CharField):
    default_error_messages = {
        'captcha_invalid': _(u'Invalid captcha')
    }

    def __init__(self, *args, **kwargs):
        #set this field's widget to the one defined in [[widgets.py]]
        self.widget = ReCaptcha
        self.required = True
        self.is_recaptcha = True
        super(ReCaptchaField, self).__init__(*args, **kwargs)

    def clean(self, values):
        super(ReCaptchaField, self).clean(values[1])
        recaptcha_challenge_value = smart_unicode(values[0])
        recaptcha_response_value = smart_unicode(values[1])
        check_captcha = captcha.submit(recaptcha_challenge_value,
            recaptcha_response_value, settings.RECAPTCHA_PRIVATE_KEY, {})
        if not check_captcha.is_valid:
            raise forms.util.ValidationError(
                    self.error_messages['captcha_invalid'])
        return values[0]

