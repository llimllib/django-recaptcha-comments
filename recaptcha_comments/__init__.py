from django.core import urlresolvers
from django.contrib.comments.models import Comment
from recaptcha_comments.forms import CommentCaptchaForm

def get_form():
    return CommentCaptchaForm
