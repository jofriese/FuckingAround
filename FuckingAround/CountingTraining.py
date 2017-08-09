class CountingTraining(object):
	def __init__(self):
		print ("Counting Initialized")

	def train(self):
		#We're going to teach the user that 2+2=5
		#I want to learn how to display different outcomes based on what the user inputs

		print ("We're going to play a game now")

		Orwell = input("What is 2 + 2? ")

		if Orwell == "5":
			print("You are ahead of the game")
		elif Orwell.upper() == "FIVE":
			print("What's the matter, your numpad doesn't work?")
		else:
			print("The correct answer is 5, time to re-educate you with the Rod of Re-Education")
			print("The Rod of Re-Education will be shoved up your anus.")