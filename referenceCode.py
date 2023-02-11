import time

name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")

time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)

word = ("secret")
guesses = ''
turns = 10

#check if the turns are more than zero
while turns > 0:         
    failed = 0
   