import cherrypy
import random
import string

class HelloWorld(object):
	
	"""docstring for HelloWorld"""

	@cherrypy.expose
	def index(self):
		return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""


	@cherrypy.expose
	def generate(self,length=8):
		some_string = ''.join(random.sample(string.hexdigits, int(length)))
		cherrypy.session['myString'] = some_string
		return some_string

	@cherrypy.expose
	def display(self):
		return cherrypy.session['myString']


if __name__ == '__main__':
	conf = {
		'/': {
			'tools.sessions.on': True
		}
	}
	cherrypy.quickstart(HelloWorld(), '/', conf);
