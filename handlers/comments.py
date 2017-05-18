import cgi

from google.appengine.api import users
from google.appengine.api import memcache

from handlers.base import BaseHandler
from models.comment import Comment


class CommentAddHandler(BaseHandler):
    def post(self, topic_id):
        csrf_token_from_form = self.request.get("csrf_token")

        csrf_memcache_result = memcache.get(csrf_token_from_form)
        if not csrf_memcache_result:
            return self.write("You are an attacker.")

        user = users.get_current_user()
        if not user:
            return self.write("You are not logged in.")

        text = cgi.escape(self.request.get("text"))

        new_comment = Comment(
            content=text,
            author_email=user.email(),
            topic_id=int(topic_id),
        )
        new_comment.put()

        return self.write("Comment created successfully.")
