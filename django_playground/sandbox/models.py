from django.db import models
from django.contrib.auth.models import User

class Thing(models.Model):
    name = models.CharField(max_length = 200)
    owners = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name
    
