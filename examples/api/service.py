# coding=utf-8

import time
from renren_client import RenrenAPIError, ErrorCode

class Service(object):
    def __init__(self, client):
        self.client = client

    def over_limit_handler(self, callback, **params):
        self.over_limit_callback = callback
        self.over_limit_callback_params = params

    def http(self, uri, **params):
        try:
            return self.client.http(uri, **params)
        except RenrenAPIError as e:
            server_c = [ErrorCode.SERVICE_UNAVAILABLE, ErrorCode.SERVICE_BUSY]
            if e.code in server_c:
                # 服务器异常
                time.sleep(20)
                return self.client.http(uri, **params)
            if e.code == ErrorCode.EXPIRED_TOKEN:
                # Token 过期
                self.client.refresh()
                return self.client.http(uri, **params)
            if e.code == ErrorCode.APP_OVER_INVOCATION_LIMIT:
                # 调用超限
                return self.over_limit_callback(**params)
        else:
            return None
