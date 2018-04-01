import os, socket, ssl, pprint, tornado.ioloop, tornado.web, tornado.httpserver
from tornado.tcpserver import TCPServer
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hi Shaun, Welcome to Tornado Web Framework.")

application = tornado.web.Application([
    (r"/", MainHandler),
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

