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
        
        else:
            print ("_",end=""),     
       
            failed += 1

    if failed == 0:        
        print ("You won")
        break
       
    guess = input("guess a character:") 
    guesses += guess                    

    if guess not in word:  
        turns -= 1        
        print ("Wrong")  
        print ("You have", + turns, 'more guesses' )
 