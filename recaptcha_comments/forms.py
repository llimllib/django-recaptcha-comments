from django import forms
from django.contrib.comments.forms import CommentForm
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from recaptcha_comments.fields import ReCaptchaField

COMMENT_MAX_LENGTH = getattr(settings,'COMMENT_MAX_LENGTH', 3000)

class CommentCaptchaForm(CommentForm):
    name          = forms.CharField(label=_("What's your name?"), max_length=50)
    email         = forms.EmailField(label=_("What's your email address?"))
    url           = forms.URLField(label=_("What's your web site (optional)?"),
                                   required=False)
    comment       = forms.CharField(label=_('Your Comment (250 words or less)'),
                                    widget=forms.Textarea,
                                    max_length=COMMENT_MAX_LENGTH)
    captcha       = ReCaptchaField()
