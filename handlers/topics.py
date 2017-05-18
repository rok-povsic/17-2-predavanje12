import cgi
import uuid

from google.appengine.api import users
from google.appengine.api import memcache

from handlers.base import BaseHandler
from models.topic import Topic
from models.comment import Comment


class TopicAddHandler(BaseHandler):
    def get(self):
        csrf_token = str(uuid.uuid4())
        memcache.add(key=csrf_token, value=True, time=600)

        params = {
            "csrf_token": csrf_token
        }
        return self.render_template("topic_add.html", params)

    def post(self):
        csrf_token_from_form = self.request.get("csrf_token")

        csrf_memcache_result = memcache.get(csrf_token_from_form)
        if not csrf_memcache_result:
            return self.write("You are an attacker.")

        user = users.get_current_user()
        if not user:
            return self.write("You are not logged in.")

        title = cgi.escape(self.request.get("title"))
        text = cgi.escape(self.request.get("text"))

        new_topic = Topic(
            title=title,
            content=text,
            author_email=user.email()
        )
        new_topic.put()

        return self.write("Topic created successfully.")


class TopicShowHandler(BaseHandler):
    def get(self, topic_id):
        csrf_token = str(uuid.uuid4())
        memcache.add(key=csrf_token, value=True, time=600)

        topic = Topic.get_by_id(int(topic_id))
        comments = Comment.query(Comment.topic_id == int(topic_id), Comment.deleted == False).fetch()
        params = {
            "topic": topic,
            "comments": comments,
            "csrf_token": csrf_token,
        }
        return self.render_template("topic_show.html", params)
