import time
import pyttsx3
from termcolor import cprint
from python_play.player import play_it

def houseEnter():
    trials = 0
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
                    if trials != 1:     
                        print("You will have attempts again after 15 mins. If you fail again, the door's alarm will ring.")
                        time.sleep(4)
                        speaker.say("Would you wait at the front door?")
                        speaker.runAndWait()
                        firstFail = input("Type Y/N \n").lower()

                        if 'y' in firstFail:
                            turns = 3
                            time.sleep(4)
                            pass
                        elif 'n' in firstFail:
                            print("You decided to go through the back door instead.")
                            speaker.say("This is the back door!")
                            time.sleep(1)
                            speaker.say("Type in your password to unlock the door.")
                            speaker.runAndWait()
                            time.sleep(0.5)
                            turns = 3
                            index+=1
                            pass

                        else:
                            trials = 1

                    if trials == 1:
                        play_it('alarm.mp3')
                        #fgdfgsgsdfg

                        time.sleep(1)
                        speaker.say("Dialing 911.. Attempt of breaking in...")
                        speaker.runAndWait()
                        time.sleep(4)
                        exit()

                    else:
                        trials+=1
                    #alarm? or calling 911

def security(singleOption, askUser):
    while singleOption == 0:
        doors = ['Front Door', 'Back Door']
        #returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
        doorCd = dict(zip(doors,code)) 
        speaker.say("Do you want to reassess your security?")
        speaker.runAndWait()

        onSecurity = input("\nType Y/N \n").lower()
        # user validationhgfhfj
        if 'y' in onSecurity:
            speaker.say("What do you want to do?")
            speaker.runAndWait()
            print('     \033[01m\033[36m1\033[0m -> \033[01mModify front door code\033[0m')
            print('     \033[01m\033[36m2\033[0m -> \033[01mModify back door code\033[0m') #design terminal
            print('     \033[01m\033[36m3\033[0m -> \033[01mModify front and back door code\033[0m')
            time.sleep(3)
            askUSer = int(input("Choose a number: "))
            #user validation
            singleOption+=1

        
            if singleOption != 0:
                if askUSer == 1:
                    speaker.say("Input the new code for front door")
                    speaker.runAndWait()
                    newCode = input("> ")
                    #from the password prog from g11dfgsdgsdg
                    doorCd["Front Door"] = newCode
                    
                elif askUSer == 2:
                    speaker.say("Input the new code for back door")
                    speaker.runAndWait()
                    newCode = input("> ")
                    #from the password prog from g11dfgsdgsdg
                    doorCd["Back Door"] = newCode
                    
                elif askUSer == 3:
                    security(singleOption+1, askUSer+1)
                    security(singleOption+1, askUSer+2)


                #else:

                time.sleep(1)
                speaker.say('Saved!')
                speaker.runAndWait()
                print('Remember your new door codes:')
                for key, value in doorCd.items():
                    print(key + " : " + value)
                break

        #elif 'n' in onSecurity:


# Driver program
if __name__ == '__main__': #executes coroutine on the default event loop
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

    houseEnter()

    askUser = 0 
    singleOption = 0 #initialize for recursion
    security(singleOption, askUser)
    #when inside change/code
    #music?
    #check business?



