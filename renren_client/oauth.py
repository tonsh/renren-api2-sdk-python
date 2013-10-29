# coding=utf-8

import json
import time
import urllib
import urllib2

class TokenType:
    """ token type """

    BEARER = 'bearer'
    MAC = 'mac'
    

class AccessToken(object):
    """ The token factory """

    OAUTH_HOST = "https://graph.renren.com/oauth"

    def __init__(self, type,
                bearer_token=None, refresh_token=None,
                mac_token=None, mac_key=None, mac_algorithm=None):
        """
            type: token type
                如果 token_type 为 bearer 类型则必须传入 bearer_token, refresh_token 参数;
                如果 token_type 为 mac 类型则必须传入 mac_token, mac_key, mac_algorithm 参数;
        """
        self.type = type
        if self.type == TokenType.MAC:
            self.token = MacToken(mac_token, mac_key, mac_algorithm)
        else:
            self.token = BearerToken(bearer_token, refresh_token)

    def get(self, uri, **params):
        uri = "%s?%s" % (uri, urllib.urlencode(params))
        return self.token._call("GET", uri)

    def post(self, uri, **params):
        return self.token._call("POST", uri, params)

    def head(self, uri, **params):
        return self.token._call("HEAD", uri, params)


class AbsToken(object):
    """ The abstraction Token class """

    API_HOST = 'api.renren.com'

    def _call(self):
        raise NotImplementedError("Subclass should implement '_fetch' method")


class MacToken(AbsToken):
    """ Mac token class """

    def __init__(self, mac_token, mac_key, mac_algorithm):
        self.schema = 'http'
        self.mac_token = mac_token
        self.mac_key = mac_key
        self.mac_algorithm = mac_algorithm

    def build_auth_header(self, uri, schema='https', method='GET'):
        # mac token signature params
        timestamp = int(time.time())
        nonce = MacToken.random_str()
        port = 80
        exts = ''

        mac_str = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (
            timestamp, nonce, method.upper(), uri, self.API_HOST, port, exts)
        mac_hashed = MacToken.build_signature(self.mac_key, mac_str)

        return 'MAC id="%s",ts="%s",nonce="%s",mac="%s"' % (
            self.mac_token, timestamp, nonce, mac_hashed)

    @staticmethod
    def random_str(length=8):
        import random

        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
        return ''.join(random.sample(chars, length))

    @staticmethod
    def build_signature(key, base_str):
        """
            生成 hmac_sha1 签名
        """
        import hmac
        import hashlib

        # key must be string, but not unicode or None
        if isinstance(key, unicode):
            key = key.encode('utf-8')

        return hmac.new(key, base_str, hashlib.sha1).digest().encode('base64').rstrip()

    def _call(self, method, uri, params=None):
        url = "%s://%s%s" % (self.schema, self.API_HOST, uri)
        header = self.build_auth_header(
            uri=uri, schema=self.schema, method=method)
        headers = {'Authorization': header}
        if params:
            params = urllib.urlencode(params)
        request = urllib2.Request(url, data=params, headers=headers)

        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            response = e

        return json.loads(response.read())


class BearerToken(AbsToken):
    """ Bearer token class """

    def __init__(self, bearer_token, refresh_token=None):
        self.schema = 'https'
        self.bearer_token = bearer_token
        self.refresh_token = refresh_token

    def build_auth_header(self):
        return "Bearer %s" % self.bearer_token

    def _call(self, method, uri, params=None):
        url = "%s://%s%s" % (self.schema, self.API_HOST, uri)
        headers = {'Authorization': self.build_auth_header()}
        if params:
            params = urllib.urlencode(params)
        request = urllib2.Request(url, data=params, headers=headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            response = e

        return json.loads(response.read())
