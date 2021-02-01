from __future__ import absolute_import
from django.conf.urls.defaults import *
from tastypie.api import Api
from gis.api.resources import GeoNoteResource, UserResource

api = Api(api_name='v1')
api.register(GeoNoteResource())
api.register(UserResource())

urlpatterns = api.urls
