from django.contrib.gis import admin
from shapeEditor.shared.models import *

# Register your models here.
admin.site.register(Shapefile, admin.ModelAdmin)
admin.site.register(Feature, admin.GeoModelAdmin)
admin.site.register(Attribute, admin.ModelAdmin)
admin.site.register(AttributeValue, admin.ModelAdmin)