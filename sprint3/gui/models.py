# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class articles(models.Model):
	title=models.CharField(max_length=1000)
	link=models.CharField(max_length=1000)
	img=models.CharField(max_length=1000)
	category=models.CharField(max_length=10)
	def __str__(self):
		return self.title