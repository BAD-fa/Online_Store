from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RatingConfig(AppConfig):
    default_auto_field  = 'django.db.models.BigAutoField'
    name = 'Rating'
    verbose_name        = _('iRating')
    verbose_name_plural = _('iRatings')
