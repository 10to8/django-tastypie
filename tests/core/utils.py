from __future__ import absolute_import
import logging


class SimpleHandler(logging.Handler):
    logged = []

    def emit(self, record):
        SimpleHandler.logged.append(record)
