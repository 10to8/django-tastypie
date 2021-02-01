from __future__ import absolute_import
from tastypie.authorization import Authorization
from tastypie.fields import CharField
from tastypie.resources import ModelResource
from alphanumeric.models import Product


class ProductResource(ModelResource):
    class Meta:
        resource_name = 'products'
        queryset = Product.objects.all()
        authorization = Authorization()
