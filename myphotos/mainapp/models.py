#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
class Photo(models.Model):
	phtitle = models.CharField(max_length=128, unique=True)
	phauthor = models.CharField(max_length=255)
	phsite = models.CharField(max_length=255)
	phnotes = models.TextField(help_text='Notes about photo')
	phimage = models.ImageField(upload_to='photos')
	phtime_registered = models.DateTimeField(auto_now=True)
	phuser = models.ForeignKey(User)

	def __unicode__(self):
		return self.phtitle
