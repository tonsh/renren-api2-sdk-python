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

    unkown = 'UNKNOW'
    service_unavailable = 'SERVICE_UNAVAILABLE'
    service_busy = 'SERVICE_BUSY'
    expired_token = 'EXPIRED-TOKEN'
    app_over_invocation_limit = 'APP_OVER_INVOCATION_LIMIT'
    user_not_exist = 'USER_NOT_EXIST'
    login_user_freeze = 'LOGIN_USER_FREEZE'
    no_right_call_this_method = 'NO_RIGHT_CALL_THIS_METHOD'
    no_such_mehtod = 'NO_SUCH_MEHTOD'
    requst_method_not_support = 'REQUST_METHOD_NOT_SUPPORT'
    illegal_tester = 'ILLEGAL_TESTER'
    permission_need = 'PERMISSION-NEED'
    login_user_banned = 'LOGIN_USER_BANNED'
    invalid_authorization_parameters = 'INVALID_AUTHORIZATION_PARAMETERS'
    login_user_suicide = 'LOGIN_USER_SUICIDE'
    method_was_closed = 'METHOD_WAS_CLOSED'
    no_right_call_this_method_deeper = 'NO_RIGHT_CALL_THIS_METHOD_DEEPER'
    no_right = 'NO_RIGHT'
    upload_file_size_exceed_limit = 'UPLOAD_FILE_SIZE_EXCEED_LIMIT'
    invalid_authorization_PARAMETERS = 'INVALID-AUTHORIZATION-PARAMETERS'
    expired_timestamp = 'EXPIRED-TIMESTAMP'
    already_used_nonce = 'ALREADY-USED-NONCE'
    invalid_signature = 'INVALID-SIGNATURE'
    invalid_token = 'INVALID-TOKEN'
    service_execution_timeout = 'SERVICE-EXECUTION-TIMEOUT'

