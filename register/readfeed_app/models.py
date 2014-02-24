from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from planet.models import Feed
import hashlib
from datetime import datetime

# Create your models here.
class App(models.Model):
  site= models.ForeignKey(Site)
  authorized = models.BooleanField(default=True)

  def __unicode__(self):
    return u"%s" % site.name

  def _create_hash(self):
    hashed = hashlib.md5()
    hashed.update(site + Datetime.now())
    return hashed.hexdigest()
  app_secret = property(_create_hash)

class Subscription(models.Model):
  # should be an intermediary model of The extended User and Feed https://docs.djangoproject.com/en/dev/topics/db/models/#extra-fields-on-many-to-many-relationships
  user = models.ForeignKey(User)
  feed = models.ForeignKey(Feed)
  creation_date = models.DateTimeField(auto_now=True, blank=True)
  #removal_hash = models.CharField(max_length=100, unique = True)
  # should add a method to create the hash
  def __unicode__(self):
    return u"%s subscribed to %s" % (self.user, self.feed)
  
  def _create_hash(self):
     hashed = hashlib.md5()
     hashed.update(user.id + feed.id + creation_date)
     return hashed.hexdigest()
  removal_hash = property(_create_hash)
#class UserProfile(models.Model):
#  user = models.OneToOneField(User)
#  subscriptions = models.One

#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
