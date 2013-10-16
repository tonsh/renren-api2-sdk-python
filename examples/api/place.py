# coding=utf-8

from service import Service

class Place(Service):

    def get_places(self, longitude, latitude, radius=500, deflection=False,
                    place_name=None, page_size=20, page=1):
        """ 根据经纬度获取地点列表 """
        params = {
            'longitude': longitude,
            'latitude': latitude,
            'radius': radius,
            'deflection': deflection,
            'placeName': place_name,
            'pageSize': page_size,
            'pageNumber': page,
        }
        places = self.http('/v2/place/list', **params) or {}

        return places.get('response', [])

    def get_feeds(self, feed_type, place_id, page_size=20, page=1):
        """ 通过地点获取新鲜事 """
        params = {
            'locationFeedType': feed_type.upper(),
            'placeId': place_id,
            'pageSize': page_size,
            'pageNumber': page,
        }
        feeds = self.http('/v2/place/feed/list', **params) or {}

        return fedds.get('response', [])

    def get_friend_feeds(self, page_size=20, page=1):
        """ 获取自己和好友的带lbs信息的feed列表 """
        params = {
            'pageNo': page,
            'pageSize': page_size,
        }
        feeds = self.http('/v2/place/friend/feed/list', **params) or {}

        return feeds.get('response', [])
