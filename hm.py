import string
import os
import random

words=[]

with open("words.txt","r") as file:
	for word in file:
		words.append(word[:-1])

word = words[random.randint(0,len(words)-1)]
letters = {char:False for char in string.ascii_lowercase}

def checkWin():
	for letter in word:
		if not letters[letter]:
			return False
	return True

def getInput():
	guess = input("Enter a character: ").lower()
	if not letters[guess]:
		letters[guess] = True

def renderString():
	string = ""
	for letter in word:
		if letter == " ":
			string += " "
		elif letters[letter]:
			string += letter
		else:
			string += "-"
	print(string)

os.system("clear")
while not checkWin():
	renderString()
	getInput()
	os.system("clear")
print("Congratulations!! You Won!!")
