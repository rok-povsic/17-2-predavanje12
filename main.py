#!/usr/bin/env python
import webapp2

from handlers.base import MainHandler, CookieAlertHandler
from handlers.topics import TopicAddHandler, TopicShowHandler, TopicDeleteHandler
from handlers.comments import CommentAddHandler
from tasks.email_new_comment import EmailNewCommentWorker
from crons.delete_topics import DeleteTopicsCron

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="cookie-alert-page"),
    webapp2.Route('/topic/add', TopicAddHandler),
    webapp2.Route('/topic/show/<topic_id:\d+>', TopicShowHandler),
    webapp2.Route('/topic/show/<topic_id:\d+>/comment/add', CommentAddHandler),
    webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDeleteHandler),
    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker),
    webapp2.Route('/cron/delete-topics', DeleteTopicsCron),
], debug=True)
