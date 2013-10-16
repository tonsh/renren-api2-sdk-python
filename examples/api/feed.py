# coding=utf-8

from service import Service

class Feed(Service):

    def get_feeds(self, feed_type, uid, page_size=20, page=1):
        """ 根据新鲜事类型获取新鲜事列表 """
        params = {
            'feedType': feed_type.upper(),
            'userId': uid,
            'pageSize': page_size,
            'pageNumber': page,
        }
        feeds = self.http('/v2/feed/list', **params) or {}

        return feeds.get('response', [])
