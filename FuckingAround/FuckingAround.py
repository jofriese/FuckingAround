#This program is meant to be my learning how to use Python, but to also make it miserable for other people to review my work
#Please let me know if any of my code is shoddy, but if the content is off in your eyes, go fuck yourself
#We start with letting the idiot know what the date is on the day this crap program is run
import datetime

from NameTraining import NameTraining
from CountingTraining import CountingTraining

def main():
	Todayisthegreatest = datetime.datetime.now()
	print("Welcome to my terrible first program in Python.")
	print("Program initiated " + Todayisthegreatest.strftime('%A, %B %d, %Y, %I:%M:%S %p'))

	NameTraining().train()
	CountingTraining().train()

if __name__== "__main__":
	main()