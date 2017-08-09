#This program is meant to be my learning how to use Python, but to also make it miserable for other people to review my work
#Please let me know if any of my code is shoddy, but if the content is off in your eyes, go fuck yourself
#We start with letting the idiot know what the date is on the day this crap program is run
import datetime
Todayisthegreatest = datetime.datetime.now()
print("Welcome to my terrible first program in Python.")
print("Prgoram initiated " + Todayisthegreatest.strftime('%A, %B %d, %Y, %I:%M:%S %p'))
#We're going to let user know that they're a faggot
#Becase on the internet everyone is automatically a faggot regardless of sexual orientation
#Basically mixing strings with print function
name = input("What is your name? ")
if name.upper() == "FAGGOT" :
    print ("Good boy!")
else:
    print("You think your name is " + name)
    print("Really though, your name is Faggot, and you're a cunt.")
    print("If you are offended thus far, you're a salty cunt.")
    print("The programmer is an ass, but that doesn't make you any less of a cunt.")
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
    
