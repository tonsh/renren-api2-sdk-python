# coding=utf-8

from service import Service
from comment import Comment

class Album(Service):

    def get(self, owner_id, album_id):
        """ 获取某个用户的某个相册 """ 
        return self.http('/v2/album/get', albumId=album_id, ownerId=owner_id)

    def get_albums(self, owner_id, page_size=20, page=1):
        """ 以分页的方式获取某个用户的相册列表 """
        params = {
            'ownerId': owner_id,
            'pageSize': page_size,
            'pageNumber': page,
        }
        albums = self.http('/v2/album/list', **params) or {}

        return albums.get('response', [])

    def get_comments(self, owner_id, album_id, page_size=20, page=1, desc=True):
        """ 评论列表
            owner_id        相册所有者的ID
            album_id        被评论对象的ID 
            page_size       页面大小。取值范围1-100，默认大小20
            page            页码。取值大于零，默认值为1
            desc            是否降序。True: 按评论时间降序 False:按评论时间升序
        """
        cmt = Comment(self.client)
        return cmt.list('album', owner_id, album_id, page_size, page, desc)

