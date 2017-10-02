# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django import forms
from django.forms import ModelForm
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
	"""docstring fos Category"""

	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Photo(models.Model):
	"""fotos del album"""

	category = models.ForeignKey(Category, null=True, blank=True)
 	title = models.CharField(max_length=50, default='No title')
 	photo = models.ImageField(upload_to='photo/')
 	pub_date = models.DateField(auto_now_add=True)
 	favorite = models.BooleanField(default=False)
 	comment = models.CharField(max_length=200, blank=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
 		return reverse('photo-list')

#	def get_form_class(self):
		"""Returns the form class to use in this view."""
#	if self.fields is not None and self.form_class:
#   		raise ImproperlyConfigured(
#        	"Specifying both 'fields' and 'form_class' is not permitted."
#    		)
#    	if self.form_class:
#        	return self.form_class
#    	else:
#    
#   			if self.model is not None:
#            # If a model has been explicitly provided, use it
#        			model = self.model
#			elif hasattr(self, 'object') and self.object is not None:
#            # If this view is operating on a single object, use
            # the class of that object
#            			model = self.object.__class__
#            		else:
            # Try to get a queryset and extract the model class
            # from that
#            			model = self.get_queryset().model

#    	if self.fields is None:
#        	raise ImproperlyConfigured(
#                "Using ModelFormMixin (base class of %s) without "
#                "the 'fields' attribute is prohibited." % self.__class__.__name__)
#        	return model_forms.modelform_factory(model, fields=self.fields)
		 	
@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
	"""Borra el fichero de las fotos que se eliminar"""
	instance.photo.delete(False)

