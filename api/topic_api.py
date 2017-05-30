import time
import json

from handlers.base import BaseHandler
from models.topic import Topic


class TopicApi(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        return self.write(json.dumps({
            "title": topic.title,
            "content": topic.content,
        }))
