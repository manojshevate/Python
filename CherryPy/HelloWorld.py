import cherrypy
import random
import string

class HelloWorld(object):
	
	"""docstring for HelloWorld"""

	@cherrypy.expose
	def index(self):
		return "Hello World!!"


	@cherrypy.expose
	def generate(self,length=8):
		return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
	cherrypy.quickstart(HelloWorld());
