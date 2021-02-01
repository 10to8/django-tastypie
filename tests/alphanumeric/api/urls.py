from __future__ import absolute_import
from django.conf.urls.defaults import *
from tastypie.api import Api
from alphanumeric.api.resources import ProductResource

api = Api(api_name='v1')
api.register(ProductResource(), canonical=True)

urlpatterns = api.urls
