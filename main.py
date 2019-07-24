# the import section
import webapp2
import jinja2
import os
import random

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file
def getPersonality(clothes1, clothes2):
	if clothes1 == "":
		print('ye')

	elif clothes1 == "":
		print('ye')

	elif clothes1 == "":
		print('ye')

	elif clothes1 == "":
		print('ye')

	elif clothes1 == "":
		print('ye')

	elif clothes1 == "":
		print('ye')
		
	if clothes2 == "":
		print('ye')
	elif clothes2 == "":
		print('ye')
	elif clothes2 == "":
		print('ye')
	elif clothes2 == "":
		print('ye')
	elif clothes2 == "":
		print('ye')
	elif clothes2 == "":
		print('ye')
# the handler section
class MainHandler(webapp2.RequestHandler):
  	def get(self):
  		welcome_template = the_jinja_env.get_template('templates/welcome.html')
		self.response.write(welcome_template.render())

class AvatarHandler(object):
	def get(self):
		print('Hello!')

	def post(self):
		print('Hello')
		avatar = self.request.get('userAvatar')
		personality = getPersonality(self.request.get(''))
		avatar = {
		"personality": personality,
		"accuracy": random.randint(0, 100)
		}
		self.response.write(welcome_template.render(avatar))


class QuizHandler(object):
	def get(self):
		quiz_template = the_jinja_env.get_template('templates/quiz.html')
		self.response.write('Hi!')
		


# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/avatar', AvatarHandler),
  ('/quiz', QuizHandler)
  ], debug=True)