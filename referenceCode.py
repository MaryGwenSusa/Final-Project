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
    
    # for every character in secret_word    
    for char in word:      
        if char in guesses:    
        # print then out the character
            print (char,end=""),