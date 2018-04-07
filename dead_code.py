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

class PageHandler(tornado.web.RequestHandler):
    def get(self):

        loader = tornado.template.Loader("templates")
        template = loader.load("simplepage.html")
        self.write(template.generate(text="templated text"))


