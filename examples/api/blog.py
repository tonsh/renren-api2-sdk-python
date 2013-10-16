# coding=utf-8

from service import Service
from comment import Comment

class Blog(Service):

    def get_blogs(self, owner_id, page_size=20, page=1):
        """ 以分页的方式获取某个用户的日志列表 """
        params = {
            'ownerId': owner_id,
            'pageSize': page_size,
            'pageNumber': page,
        }
        albums = self.http('/v2/blog/list', **params) or {}

        return albums.get('response', [])

    def get(self, owner_id, blog_id, password=None):
        """ 获取某个用户的某篇日志 """
        params = {
            'ownerId': owner_id,
            'blogId': blog_id,
            'password': password,
        }
        return self.http('/v2/blog/get', **params)

    def get_comments(self, owner_id, blog_id, page_size=20, page=1, desc=True):
        """ 评论列表
            owner_id    日志所有者的ID
            blog_id     被评论日志的ID 
            page_size   页面大小。取值范围1-100，默认大小20
            page        页码。取值大于零，默认值为1
            desc        是否降序。True: 按评论时间降序 False:按评论时间升序
        """
        cmt = Comment(self.client)
        return cmt.list('blog', owner_id, blog_id, page_size, page, desc)

