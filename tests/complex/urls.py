from __future__ import absolute_import
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^api/', include('complex.api.urls')),
)
