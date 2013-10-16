# coding=utf-8

from service import Service
from comment import Comment

class Status(Service):

    def get_statuses(self, owner_id, page_size=20, page=1):
        """ 获取用户状态列表 """
        params = {
            'ownerId': owner_id,
            'pageSize': page_size,
            'pageNumber': page,
        }
        statuses = self.http('/v2/status/list', **params) or {}

        return statuses.get('response', [])

    def get(self, owner_id, status_id):
        """ 获取用户状态 """
        return self.http('/v2/status/get', ownerId=owner_id, statusId=status_id)

    def get_comments(self, owner_id, status_id,
                    page_size=20, page=1, desc=True):
        """ 评论列表
            owner_id    状态所有者的ID
            status_id   状态ID 
            page_size   页面大小。取值范围1-100，默认大小20
            page        页码。取值大于零，默认值为1
            desc        是否降序。True: 按评论时间降序 False:按评论时间升序
        """
        cmt = Comment(self.client)
        return cmt.list('status', owner_id, status_id, page_size, page, desc)

