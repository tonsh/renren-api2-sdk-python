#coding=utf-8

from service import Service

class User(Service):
    
    def get(self, uid):
        """ 获取用户信息 """
        return self.http('/v2/user/get', userId=uid)

    def profile(self, uid):
        """ 获取用户的主页信息，包括各种统计数据 """
        return self.http('/v2/profile/get', userId=uid)

    def batch(self, uids):
        """ 批量获取用户信息
            uids: uid 列表
        """
        if not uids:
            return None

        uids = ','.join([str(uid) for uid in uids])
        users = self.http('/v2/user/batch', userIds=uids) or {}

        return users.get('response', [])

    def get_friends(self, uid, page_size=20, page=1):
        """ 获取某个用户的好友列表 """
        params = {
            'userId': uid,
            'pageSize': page_size,
            'pageNumber': page,
        }
        friends = self.http('/v2/user/friend/list', **params) or {}

        return friends.get('response', [])
    
    def get_friend_ids(self, uid, page_size=500, page=1):
        """ 获取某个用户的好友ID列表 """
        params = {
            'userId': uid,
            'pageSize': page_size,
            'pageNumber': page,
        }
        fids = self.http('/v2/friend/list', **params) or {}

        return fids.get('response', [])

    def vipinfo(self, uid):
        """ 获取某个用户的VIP信息 """
        vipinfo = self.http('/v2/vipinfo/get', userId=uid) or {}

        return vipinfo.get('response', None)

