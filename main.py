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
	if clothes1 == "short-sleeve1":
		personality = "You are a stand out person with a strong personality"

	elif clothes1 == "short-sleeve2":
		personality = "You keep to yourself, but you have a pretty cool personality"

	elif clothes1 == "short-sleeve3":
		personality = "You are quite shy, even though you are actually a dope person, you have a passive personality"

	elif clothes1 == "long-sleeve1":
		print('ye')

	elif clothes1 == "long-sleeve2":
		print('ye')

	elif clothes1 == "long-sleeve3":
		print('ye')
		
	if clothes2 == "pants1":
		print('ye')
	elif clothes2 == "pants2":
		print('ye')
	elif clothes2 == "pants3":
		print('ye')
	elif clothes2 == "shorts1":
		print('ye')
	elif clothes2 == "shorts2":
		print('ye')
	elif clothes2 == "shorts3":
		print('ye')
# the handler section
class MainHandler(webapp2.RequestHandler):
  	def get(self):
  		welcome_template = the_jinja_env.get_template('templates/welcome.html')
		self.response.write(welcome_template.render())

class AvatarHandler(webapp2.RequestHandler):
	def get(self):
		create_template = the_jinja_env.get_template('templates/avatar.html')
		self.response.write(create_template.render())

class ResultsHandler(object):
	def post(self):
		results_template = the_jinja_env.get_template('templates/results.html')
		avatar = self.request.get('userAvatar')
		personality = getPersonality(self.request.get(''))
		avatar = {
		"personality": personality,
		"accuracy": random.randint(0, 100)
		}
		self.response.write(results_template.render())


class QuizHandler(webapp2.RequestHandler):
	def get(self):
		quiz_template = the_jinja_env.get_template('templates/quiz.html')
		self.response.write(quiz_template.render())
		


# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/avatar', AvatarHandler),
  ('/quiz', QuizHandler),
  ('/results', ResultsHandler)
  ], debug=True)