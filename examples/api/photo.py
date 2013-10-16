# coding=utf-8

from service import Service
from comment import Comment

class Photo(Service):

    def get_photos(self, owner_id, album_id, page_size=20, page=1,
                    password=None):
        """ 以分页的方式获取某个用户某个相册里的照片列表 """
        params = {
            'ownerId': owner_id,
            'albumId': album_id,
            'pageSize': page_size,
            'pageNumber': page,
            'password': password,
        }
        albums = self.http('/v2/photo/list', **params) or {}

        return albums.get('response', [])

    def get(self, owner_id, album_id, photo_id, password=None):
        """ 获取某个用户某个相册里的某张照片 """
        params = {
            'photoId': photo_id,
            'albumId': album_id,
            'ownerId': owner_id,
            'password': password,
        }
        return self.http('/v2/photo/get', **params)
    
    def get_comments(self, owner_id, photo_id, page_size=20, page=1, desc=True):
        """ 评论列表
            owner_id        photo 所有者的ID
            entry_id        photo ID 
            page_size       页面大小。取值范围1-100，默认大小20
            page            页码。取值大于零，默认值为1
            desc            是否降序。True: 按评论时间降序 False:按评论时间升序
        """
        cmt = Comment(self.client)
        return cmt.list('photo', owner_id, photo_id, page_size, page, desc)

