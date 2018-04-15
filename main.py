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
import blockchain_api
from blockchain_api import TransactionDetails
class BlockchainAddy(Form):
    address = wtforms.TextField(
        'Address', validators=[wtforms.validators.DataRequired()], default=u'')


class BlockchainQuery(tornado.web.RequestHandler):
    def get(self):
        form = BlockchainAddy()
        loader = tornado.template.Loader("templates")
        template = loader.load("blockchainaddy.html")
        self.write(template.generate(form=form))

    def post(self):
        form = BlockchainAddy(self.request.arguments)
        details = ''
        if form.validate():
            for f in self.request.arguments:
                details += self.get_argument(f, default=None, strip=False)
            loader = tornado.template.Loader("templates")
            template = loader.load("address_template.html")
            input_details = blockchain_api.read_blockchain_address(details)

            self.write(template.generate(address=details, details = input_details))
        else:
            self.set_status(400)
            self.write(form.errors)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hi Shaun, Welcome to Tornado Web Framework.")


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/blockchain_addy", BlockchainQuery),
])

# implementation for SSL
# http_server = tornado.httpserver.HTTPServer(application, ssl_options={
#     "certfile": os.path.join(os.environ['HOME'], ".ssh", "dev.shaun-dev.com.crt"),
#     "keyfile": os.path.join(os.environ['HOME'], ".ssh", "dev.shaun-dev.com.key"),
# })

if __name__ == "__main__":
    application.listen(int(os.environ['PORT']))
    #http_server.listen(int(os.environ['PORT']))
    tornado.ioloop.IOLoop.instance().start()
