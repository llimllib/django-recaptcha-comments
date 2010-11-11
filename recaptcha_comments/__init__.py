from django.core import urlresolvers
from django.contrib.comments.models import Comment
from recaptcha_comments.forms import CommentCaptchaForm

#Override the default django form with our CommentCaptchaForm. See 
#the [django documentation](http://docs.djangoproject.com/en/dev/ref/contrib/comments/custom/)
#for more details
def get_form():
    return CommentCaptchaForm
