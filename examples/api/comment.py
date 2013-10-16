# coding=utf-8

from service import Service

class Comment(Service):

    def list(self, comment_type, entry_owner_id, entry_id,
            page_size=20, page=1, desc=True):
        """ 评论列表
            entry_owner_id  评论对象所有者的ID
            entry_id        被评论对象的ID 
            page_size       页面大小。取值范围1-100，默认大小20
            page            页码。取值大于零，默认值为1
            desc            是否降序。True: 按评论时间降序 False:按评论时间升序
        """
        params = {
            'commentType': comment_type.upper(),
            'entryId': entry_id,
            'entryOwnerId': entry_owner_id,
            'pageSize': page_size,
            'pageNumber': page,
            'desc': desc,
        }
        comments = self.http('/v2/comment/list', **params) or {}
        
        return comments.get('response', [])

