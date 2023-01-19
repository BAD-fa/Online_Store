from django.contrib import admin

from . import models


admin.site.register(models.Rating)
admin.site.register(models.RatedItem)