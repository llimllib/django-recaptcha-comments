from django.contrib.comments.forms import CommentForm

from recaptcha_comments.fields import ReCaptchaField

# To customize the comment form, you can uncomment any or all of these
# lines, move them into the CommentCaptchaForm class, and edit the
# characteristics of the field you want to change. See
# django's form fields documentation
# [http://docs.djangoproject.com/en/dev/ref/forms/fields/](here)
#
# You may need some or all of these imports:
# from django.conf import settings
# from django import forms
# from django.utils.translation import ungettext, ugettext_lazy as _
#
# and the comment field requires this line at the module level:
# COMMENT_MAX_LENGTH = getattr(settings,'COMMENT_MAX_LENGTH', 3000)
#
#name          = forms.CharField(label=_("Name"), max_length=50)
#email         = forms.EmailField(label=_("Email address"))
#url           = forms.URLField(label=_("URL"),
#                               required=False)
#
#comment       = forms.CharField(label=_('Comment'),
#                                widget=forms.Textarea,
#                                max_length=COMMENT_MAX_LENGTH)
class CommentCaptchaForm(CommentForm):
    captcha       = ReCaptchaField()
