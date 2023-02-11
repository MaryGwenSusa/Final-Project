import time
import pyttsx3

speaker = pyttsx3.init() #initialize
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 155) #adjusted the speed of reading since its default 200 is too fast

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) #change voice for female through changing its index since default is male still male index is 0

speaker.say("This is the front door!")
speaker.runAndWait()
time.sleep(1)
print("Type in your password to unclock the door.")
time.sleep(0.5)

code = "0p3nd00R"
attempts = ""
turns = 3

#check if the turns are more than zero
while turns > 0:         
    failed = 0

    # for every character in code    
    for char in code:
        if char not in attempts:
            print ("_",end=""), 
            failed += 1

    if failed == 0:        
        print ("\nUnlocking...")
        time.sleep(1)
        print ("Welcome! You may come in.")
        break

