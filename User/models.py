from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blog(models.Model):
	users = models.ForeignKey(User,on_delete = models.CASCADE)
	text = models.TextField(unique=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __str__(self):
		return self.text
