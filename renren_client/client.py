# coding=utf=8

import json
import urllib
import urllib2
import logging
import traceback
from ConfigParser import ConfigParser
from oauth import AccessToken
from method import API_METHOD
from error import ErrorCode, RenrenAPIError

def logger_record(func):
    def wrapper(*args, **kargs):
        log_filename = args[0].log_filename
        log_level = args[0].log_level

        logging.basicConfig(
            filename=log_filename,
            level=log_level,
            format="%(asctime)s - %(levelname)s: %(message)s"
        )

        try:
            return func(*args, **kargs)
        except Exception:
            msg = "%s %s %s %s" % (func, ''.join(args), urllib.urlencode(kargs),
                                    traceback.format_exc())
            logging.error(msg)
            raise

    return wrapper

def logger_api(func):
    def wrapper(inst, uri, **params):
        log_filename = inst.log_filename

        logging.basicConfig(
            filename=log_filename,
            level=logging.NOTSET,
            format="%(asctime)s - %(levelname)s: %(message)s"
        )

        try:
            rst = func(inst, uri, **params)

            if isinstance(rst, dict):
                error = rst.get('error', None)
                if error:
                    code = error.get('code')
                    msg = error.get('message', u'错误')
                    raise RenrenAPIError(code, msg)

            return rst
        except Exception:
            msg = "%s %s %s" % (uri, urllib.urlencode(params),
                                traceback.format_exc())
            logging.error(msg)
            raise

    return wrapper


class RenrenClient(object):
    """
        RenrenClient 实现了 Renren API 的封装调用及认证流程。
    """

    OAUTH_HOST = "https://graph.renren.com/oauth"
    _instance = None

    def __init__(self, config_file):
        config = ConfigParser()
        config.read(config_file)

        self.client_id = config.get('app', 'app-key')
        self.client_secret = config.get('app', 'app-secret')
        self.redirect_uri = config.get('app', 'auth-redirect-uri')
        self.token_type = config.get('token', 'type')
        
        self.log_filename = config.get('logger', 'filename')
        self.log_level = config.get('logger', 'level').upper()

    @classmethod
    def instance(cls, config_file):
        if not cls._instance:
            cls._instance = cls(config_file)

        return cls._instance

    def __repr__(self):
        return '<RenrenClient Class>'

    def reset_token(self, response):
        params = {
            'bearer_token': response.get('access_token'),
            'refresh_token': response.get('refresh_token'),
            'mac_algorithm': response.get('mac_algorithm'),
            'mac_token': response.get('access_token'),
            'mac_key': response.get('mac_key'),
            'mac_algorithm': response.get('mac_algorithm'),
        }

        self.token = AccessToken(self.token_type, **params)

    @property
    def authorize_url(self):
        url = "%s/authorize?response_type=code&client_id=%s&redirect_uri=%s" % (
            self.OAUTH_HOST, self.client_id, self.redirect_uri)
        return url

    def auth_with_code(self, code):
        params = {
            'grant_type': 'authorization_code',
            'token_type': self.token_type,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'code': code,
        }
        url = "%s/token?%s" % (self.OAUTH_HOST, urllib.urlencode(params))
        response = json.loads(urllib2.urlopen(url).read())

        self.reset_token(response)

        return response

    @logger_record
    def auth_with_token(self,
            bearer_token=None, refresh_token=None,
            mac_token=None, mac_key=None, mac_algorithm=None):
        params = {
            'bearer_token': bearer_token,
            'refresh_token': refresh_token,
            'mac_token': mac_token,
            'mac_key': mac_key,
            'mac_algorithm': mac_algorithm,
        }
        self.token = AccessToken(self.token_type, **params)

    @logger_record
    def refresh(self, refresh_token):
        params = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        url = "%s/token?%s" % (self.OAUTH_HOST, urllib.urlencode(params))

        response = json.loads(urllib2.urlopen(url).read())

        self.reset_token(response)

        return response
    
    @logger_api
    def http(self, uri, **params):
        method = API_METHOD.get(uri) or 'get'
        return getattr(self.token, method)(uri, **params)
