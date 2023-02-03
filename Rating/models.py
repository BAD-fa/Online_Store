import datetime

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from Rating.managers import *


class Rating(models.Model):
	"""
	Model definition of Rating.
	---------------------------

	Arguments:
	----------
		- rated_object (fk):
			-> the object associated.
		- user (fk):
			-> the user associated.
		- rating (int):
			-> the rating associated.
		- date (datetime):
			-> the date associated.
    Managers:
    ---------
		- RatingManager:
			-> get ratings average.
	"""
	rated_object = models.ForeignKey('RatedItem', on_delete=models.CASCADE, related_name='ratings')
	user 	     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
	rating 		 = models.PositiveSmallIntegerField()
	date 		 = models.DateTimeField(_('rated on'), editable=False)
	objects 	 = RatingManager()

	def __unicode__(self):
		""" String representation of rating. """
		return f"{self.rated_object}: {self.rating} by: {self.user}"

	def __str__(self):
		""" String representation of rating. """
		return self.__unicode__()

	def __repr__(self):
		""" String representation of rating. """
		return self.__unicode__()

	def save(self, *args, **kwargs):
		if not self.id:
			self.date = datetime.datetime.now()
		super(Rating, self).save(*args, **kwargs)


class RatedItem(models.Model):
	"""
	Model definition of Rate info for an object.
	--------------------------------------------

	Arguments:
	----------
		- rating_average (decimal):
			-> the average of rates.
		- rating_count (int):
			-> the count of rates.
		- date_last_rated (datetime):
			-> the last time one rate was added.
	Methods:
	--------
		- add_or_update_rating()
		- get_average()
	Managers:
	---------
		- RatedItemManager:
			-> add or update ratings.
	"""
	rating_average  = models.DecimalField(max_digits=7, decimal_places=2)
	rating_count    = models.PositiveIntegerField()
	date_last_rated = models.DateTimeField(editable=False, null=True)

	content_type 	= models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id    	= models.PositiveIntegerField()
	content_object  = GenericForeignKey('content_type', 'object_id')

	objects 	 	= RatedItemManager()

	class Meta:
		""" Meta definition of Rating. """
		unique_together = (('content_type', 'object_id'),)

	def add_or_update_rating(self, value, user):
		now = datetime.datetime.now()
		rating, created   = Rating.objects.get_or_create(
			user 		  = user,
			rated_object  = self,
			defaults 	  = {
				'date': now,
				'rating': value
			}
		)

		if not created:
			rating.rating = value
			rating.date   = now
			rating.save()
			self.rating_count    = self.ratings.count()
			self.rating_average  = str(Rating.objects.rating_average(self.object))
			self.date_last_rated = now
			self.save()
			return self

	def get_average(self):
		return '%.1f' % self.rating_average

	def save(self, *args, **kwargs):
		if not self.id:
			self.rating_count   = 0
			self.rating_average = 0
		super(RatedItem, self).save(*args, **kwargs)