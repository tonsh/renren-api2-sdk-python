# coding=utf-8

class RenrenAPIError(Exception):
    """ Renren API exception class."""
    def __init__(self, code, msg):
        self.type, self.code = code.split('.')
        self.code = self.code.upper()
        self.msg = msg

    def __repr__(self):
        return '<RenrenAPIError Class>'

    def __unicode__(self):
        return '%s.%s - %s' % (self.type, self.code, self.msg)

    def __str__(self):
        return unicode(self).encode('utf-8')


class ErrorCode:
    SERVICE_UNAVAILABLE = 'SERVICE_UNAVAILABLE '
    SERVICE_BUSY = 'SERVICE_BUSY'
    EXPIRED_TOKEN = 'EXPIRED-TOKEN'
