# coding=utf-8

import time
from renren_client import RenrenAPIError, ErrorCode

class Service(object):
    def __init__(self, client):
        self.client = client

    def http(self, uri, **params):
        try:
            return self.client.http(uri, **params)
        except RenrenAPIError as e:
            server_c = [ErrorCode.SERVICE_UNAVAILABLE, ErrorCode.SERVICE_BUSY]
            if e.code in server_c:
                time.sleep(20)
                return self.client.http(uri, **params)
            if e.code == ErrorCode.EXPIRED_TOKEN:
                self.client.refresh()
        else:
            return None
