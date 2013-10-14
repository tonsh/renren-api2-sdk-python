# coding=utf-8

class RenrenAPIError(Exception):
    """ Renren API exception class."""
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __repr__(self):
        return '<RenrenAPIError Class>'

    def __unicode__(self):
        return 'RenrenAPIError: %s - %s' % (self.code, self.msg)

    def __str__(self):
        return unicode(self).encode('utf-8')

class ErrorCode:
    SERVICE_UNAVAILABLE = 1
    EXPIRED_TOKEN = 7
