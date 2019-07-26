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
def getSkin(tone):
	if tone == "tone1":
		skinTone = "body.png"

	elif tone == "tone2":
		skinTone = "body1.png"

	elif tone == "tone3":
		skinTone = "body2.png"

	return skinTone

def getHair(hair):
	if hair == "hair1":
		hairStyle = "hairG.png"

	elif hair == "hair2":
		hairStyle = "hairG1.png"

	elif hair == "hair3":
		hairStyle = "hairB1.png"

	elif hair == "hair4":
		hairStyle = "hairB.png"

	return hairStyle
	
def getShirt(shirt):	
	if shirt == "ss1":
		shirtType = "shirt2.png"

	elif shirt == "ss2":
		shirtType = "shirt1.png"

	elif shirt == "ss3":
		shirtType = "shirt.png"

	elif shirt == "ls1":
		shirtType = "Lshirt1.png"

	elif shirt == "ls2":
		shirtType = "Lshirt.png"

	elif shirt == "ls3":
		shirtType = "Lshirt2.png"

		return shirtType


def getPants(pants):
	if pants == "s1":
		pantsType = "shorts2.png"

	elif pants == "s2":
		pantsType = "shorts1.png"

	elif pants == "s3":
		pantsType = "shorts.png"

	elif pants == "j1":
		pantsType = "pants1.png"

	elif pants == "j2":
		pantsType = "pants2.png"

	elif pants == "j3":
		pantsType = "pants.png" 

	return pantsType 

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
		
		skinTone = getSkin(self.request.get('Skin'))
		hairStyle = getHair(self.request.get('Hair'))
		shirtType = getShirt(self.request.get('Shirt'))
		pantsType = getPants(self.request.get('Pants'))

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