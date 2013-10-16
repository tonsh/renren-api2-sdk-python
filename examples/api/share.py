# coding=utf-8

from service import Service
from comment import Comment

class Share(Service):

    def get_shares(self, owner_id, page_size=20, page=1):
        """ 获取用户分享列表 """
        params = {
            'ownerId': owner_id,
            'pageSize': page_size,
            'pageNumber': page,
        }
        shares = self.http('/v2/share/list', **params) or {}

        return shares.get('response', [])

    def get(self, owner_id, share_id):
        """ 获取某个用户的某个分享 """
        return self.http('/v2/share/get', shareId=share_id, ownerId=owner_id)
    
    def get_hots(self, share_type, page_size=20, page=1):
        """ 获取人人推荐资源 """
        share_type = ('type_%s' % share_type).upper()
        params = {
            'shareType': share_type,
            'pageSize': page_size,
            'pageNumber': page,
        }
        shars = self.http('/v2/share/hot/list', **params) or {}

        return shars.get('response', [])

    def get_comments(self, owner_id, share_id, page_size=20, page=1, desc=True):
        """ 评论列表
            owner_id        分享所有者的ID
            share_id        分享的ID 
            page_size       页面大小。取值范围1-100，默认大小20
            page            页码。取值大于零，默认值为1
            desc            是否降序。True: 按评论时间降序 False:按评论时间升序
        """
        cmt = Comment(self.client)
        return cmt.list('share', owner_id, share_id, page_size, page, desc)

