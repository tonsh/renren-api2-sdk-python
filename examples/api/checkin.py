#coding=utf-8

from service import Service

class Checkin(Service):

    def get_checkin(self, page_size=20, page=1):
        """ 获取签到列表 """
        params = {
            'pageNo': page,
            'pageSize': page_size,
        }
        checkin = self.http('/v2/checkin/list', **params) or {}

        return checkin.get('response', [])

    def get(self, checkin_id):
        """ 获取签到信息 """
        return self.http('/v2/checkin/get', checkinId=checkin_id)

    def get_replies(self, checkin_id, page_size=20, page=1):
        """ 获取签到回复列表 """
        params = {
            'checkinId': checkin_id,
            'pageNo': page_size,
            'pageSize': page_size,
        }
        replies = self.http('/v2/reply/list', **params) or {}
        
        return replies.get('response', [])

