#coding=utf-8

from service import Service

class Ubb(Service):

    def get_ubbs(self):
        """ 获取人人网ubb列表 """
        ubbs = self.http('/v2/ubb/list') or {}

        return ubbs.get('response', [])
