# coding=utf-8
""" 基于 Tornado 实现的认证流程 """

import tornado.ioloop
import tornado.web
from renren_client import RenrenClient

client = RenrenClient('config.demo.cfg')

class BaseHandler(tornado.web.RequestHandler):
    """ token 基类 """

    def request_args(self):
        """ 处理 tornado request 返回的List化的参数 """
        params = self.request.arguments
        result = {}
        for key in params:
            result[key] = self.get_argument(key)
        return result

class IndexHandler(BaseHandler):
    """ 授权 """

    def get(self):
        self.redirect(client.authorize_url, permanent=True)

class AuthHandler(BaseHandler):
    """ Code 认证 """
    def get(self):
        args = self.request_args()
        code = args.get('code', None)

        client.auth_with_code(code)
        user = client.http('/v2/user/get', userId=230387247)
        self.write(user)


application = tornado.web.Application([
    (r"/token", IndexHandler),
    (r"/token/auth", AuthHandler),
])

if __name__ == '__main__':
    application.listen(5010)
    tornado.ioloop.IOLoop.instance().start()

