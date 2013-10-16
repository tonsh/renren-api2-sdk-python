# coding=utf-8

from service import Service

class Evaluation(Service):

    def get_replies(self, owner_id, evaluation_id, page_size=20, page=1):
        """ 签到回复列表 """
        params = {
            'ownerId': owner_id,
            'evaluationId': evaluation_id,
            'pageNo': page,
            'pageSize': page_size,
        }

        replies = self.http('/v2/evaluation/reply/list', **params) or {}

        return replies.get('response', [])
