from django.db import models
from django.contrib import auth

class Blog(models.Model):
	title = models.CharField(max_length = 100)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('auth.User',null=True,related_name='blogs')
	class Meta:
		ordering = ('created',)
