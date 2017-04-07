# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Film(models.Model):
	url = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		print type(self)
		print '*****************'
		return self.url
