import os
import socket
import ssl
import pprint
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.template
from tornado.tcpserver import TCPServer
import tornado.ioloop
import tornado.web
import wtforms
from wtforms_tornado import Form


class EasyForm(Form):
    name = wtforms.TextField(
        'name', validators=[wtforms.validators.DataRequired()], default=u'test')
    email = wtforms.TextField('email', validators=[
                              wtforms.validators.Email(), wtforms.validators.DataRequired()])
    message = wtforms.TextAreaField(
        'message', validators=[wtforms.validators.DataRequired()])


class SimpleForm(tornado.web.RequestHandler):
    def get(self):
        form = EasyForm()
        loader = tornado.template.Loader("templates")
        template = loader.load("simpleform.html")
        self.write(template.generate(form=form))

    def post(self):
        form = EasyForm(self.request.arguments)
        details = ''
        if form.validate():
            for f in self.request.arguments:
                details += self.get_argument(f, default=None, strip=False)
            self.write(details)
        else:
            self.set_status(400)
            self.write(form.errors)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hi Shaun, Welcome to Tornado Web Framework.")


class PageHandler(tornado.web.RequestHandler):
    def get(self):

        loader = tornado.template.Loader("templates")
        template = loader.load("simplepage.html")
        self.write(template.generate(text="templated text"))


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/simple", SimpleForm),
    (r"/page", PageHandler)
])

# implementation for SSL
http_server = tornado.httpserver.HTTPServer(application, ssl_options={
    "certfile": os.path.join("/home/shaun/.ssh", "dev.shaun-dev.com.crt"),
    "keyfile": os.path.join("/home/shaun/.ssh", "dev.shaun-dev.com.key"),
})

if __name__ == "__main__":
    # application.listen(8888)
    http_server.listen(8443)
    tornado.ioloop.IOLoop.instance().start()
