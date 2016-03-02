import random
import string

import cherrypy

class stringGeneratorWebService(object):
	"""docstring for stringGeneratorWebService"""
	
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	def GET(self):
		return cherrypy.session['myString']


	def POST(self, length=8):
		some_string = ''.join(random.sample(string.hexdigits, int(length)))
		cherrypy.session['myString'] = some_string
		return some_string
		

	def PUT(self, some_string):
		cherrypy.session['myString'] = some_string


	def DELETE(self):
		cherrypy.session.pop('myString', None)



if __name__ == '__main__':
	conf = {
		'/': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
	        'tools.sessions.on': True,
	        'tools.response_headers.on': True,
	        'tools.response_headers.headers': [('Content-Type', 'text/plain')],
		}
	}

	cherrypy.quickstart(stringGeneratorWebService(),'/',conf)