from google.appengine.api import users

from handlers.base import BaseHandler
from models.topic import Topic

class TopicAddHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")

    def post(self):
        user = users.get_current_user()
        if not user:
            return self.write("You are not logged in.")

        title = self.request.get("title")
        text = self.request.get("text")

        new_topic = Topic(
            title=title,
            content=text,
            author_email=user.email()
        )
        new_topic.put()

        return self.write("Topic created successfully.")
