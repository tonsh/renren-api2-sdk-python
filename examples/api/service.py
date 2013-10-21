# coding=utf-8

import time
from renren_client import RenrenAPIError, ErrorCode

class Service(object):
    def __init__(self, client):
        self.client = client

    def http(self, uri, **params):
        return self.client.http(uri, **params)
