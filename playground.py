import time
import pyttsx3
from termcolor import cprint

speaker = pyttsx3.init() #initialize
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 155) #adjusted the speed of reading since its default 200 is too fast

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) #change voice for female through changing its index since default is male still male index is 0

speaker.say("This is the front door!")
time.sleep(1) #add delay
speaker.say("Type in your password to unlock the door.")
speaker.runAndWait()
time.sleep(0.5)

code = ['0p3nd00R', 'b@ckd00R']
attempts = ""
turns = 3

index = 0
entering = True

while entering == True:
    #check if the turns are more than zero
    while turns > 0:         
        failed = 0

        # for every character in code    
        for char in code[index]:
            if char not in attempts:
                print("_",end=""), 
                failed += 1

        if failed == 0:        
            cprint("\nUnlocking...", "green")
            time.sleep(1)
            speaker.say("Welcome! You may come in.")
            speaker.runAndWait()
            break
        entering = False
            
        guess = input("\n") 
        attempts += guess

        if guess != code[index]:    
            turns -= 1        
            speaker.say("Invalid.")
            speaker.runAndWait()
            print("You have \033[31m{}\033[0m more attempts.".format(turns))

            if turns == 0:           
                print("You will have attempts again after 15 mins. If you fail again, the door's alarm will ring.")
                #alarm? or calling 911
                time.sleep(4)
                speaker.say("Would you wait at the front door?")
                speaker.runAndWait()
                firstFail = input("Type Y/N \n").lower()

                if 'y' in firstFail:
                    turns = 3
                    time.sleep(4)
                    pass
                elif 'n' in firstFail:
                    index+=1
                    print("You decided to go through the back door instead.")
                    speaker.say("This is the back door!")
                    time.sleep(1)
                    speaker.say("Type in your password to unlock the door.")
                    speaker.runAndWait()
                    time.sleep(0.5)
                    turns = 3
                    pass

def security():
    speaker.say("Do you want to reassess your security?")
    speaker.runAndWait()

    onSecurity = input("Type Y/N \n").lower()
    # user validation
    if 'y' in onSecurity:
        """""   1 -> Modify front door code
                2 -> Modify back door code"""
        print(security.__doc__)
        
    elif 'n' in onSecurity:

    
#when inside change/code
#music?
#check business?



