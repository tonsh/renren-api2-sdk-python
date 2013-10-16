#coding=utf-8

from service import Service

class Like(Service):

    def get_infos(self, like_type, ugc_id, with_users=False, limit=20):
        """ 获取站内资源被赞的次数 """
        params = {
            'likeUGCType': like_type.upper(),
            'ugcId': ugc_id,
            'withLikeUsers': with_users,
            'limit': limit,
        }
        infos = self.http('/v2/like/ugc/info/get', **params) or {}

        return infos
