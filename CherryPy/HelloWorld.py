import cherrypy
import random
import string

class HelloWorld(object):
	
	"""docstring for HelloWorld"""

	@cherrypy.expose
	def index(self):
		return "Hello World!!"


	@cherrypy.expose
	def generate(self):
		return ''.join(random.sample(string.hexdigits, 8))


if __name__ == '__main__':
	cherrypy.quickstart(HelloWorld());
