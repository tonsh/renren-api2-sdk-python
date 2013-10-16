# coding=utf-8

from service import Service

class Location(Service):

    def get(self, longitude, latitude, deflection=False):
        params = {
            'longitude': longitude,
            'latitude': latitude,
            'deflection': deflection,
        }
        return self.http('/v2/location/get', **params)

    def get_feeds(self, feed_type, longitude, latitude, radius=500,
                    page_size=20, page_number=1):
        """ 通过经纬度获取新鲜事 """
        params = {
            'locationFeedType': feed_type.upper(),
            'longitude': longitude,
            'latitude': latitude,
            'radius': radius,
            'pageSize': page_size,
            'pageNumber': page_number,
        }
        feeds = self.http('/v2/location/feed/list', **params) or {}

        return feeds.get('response', [])
