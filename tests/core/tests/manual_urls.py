from __future__ import absolute_import
from django.conf.urls.defaults import *
from core.tests.resources import NoteResource


note_resource = NoteResource()

urlpatterns = patterns('',
    (r'^', include(note_resource.urls)),
)
