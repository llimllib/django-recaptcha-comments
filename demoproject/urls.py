from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', "demoapp.views.homepage"),
    (r'^templatetag.html$', "demoapp.views.templatetag"),
    (r'^comments/', include('django.contrib.comments.urls')),
)
