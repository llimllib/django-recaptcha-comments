from django.db import models

#we need an object to attach comments to, so here's a dead simple object
class Homepage(models.Model):
    def __unicode__(self):
        return "An empty object representing the home page"
