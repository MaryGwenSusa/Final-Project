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

def security():
        doors = ['Front Door', 'Back Door']
        #returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
        doorCd = dict(zip(doors,code)) 
        speaker.say("Do you want to reassess your security?")
        speaker.runAndWait()
        errorMenu = False
        justView = False
        while True:
            if errorMenu == False:
                onSecurity = input("\nType Y/N \n").lower()           
            elif errorMenu == True:
                onSecurity = 'y'

            if 'y' in onSecurity:
                speaker.say("What do you want to do?")
                speaker.runAndWait()
                print('\n     \033[01m\033[36m1\033[0m -> \033[01mModify front door code\033[0m')
                print('     \033[01m\033[36m2\033[0m -> \033[01mModify back door code\033[0m') #design terminalfhgf
                print('     \033[01m\033[36m3\033[0m -> \033[01mModify front and back door code\033[0m')
                print('     \033[01m\033[36m4\033[0m -> \033[01mView the codes\033[0m')

                time.sleep(2)
                try:
                    askUser = int(input("\nChoose a number: "))
                # ValueError is an exception that occurs when a function receives an argument of the correct data type but an inappropriate value.
                # The TypeError object represents an error when an operation could not be performed, typically (but not exclusively) when a value is not of the expected type.
                except ValueError:
                    speaker.say('That was confusing. Please clarify.')
                    speaker.runAndWait()
                    time.sleep(1)
                    errorMenu = True
                    
                    continue

                if askUser == 1:
                    speaker.say("Input the new code for front door")
                    speaker.runAndWait()
                    print(validPassword.__doc__)
                    newCode = validPassword()
                    try:
                        doorCd["Front Door"] = newCode
                    except TypeError:
                        speaker.say('There seems to be a problem on my system. I apologize. Please try again.')
                        speaker.runAndWait()
                        newCode = validPassword()
                        doorCd["Front Door"] = newCode
                                
                elif askUser == 2:
                    speaker.say("Input the new code for back door")
                    speaker.runAndWait()
                    print(validPassword.__doc__)
                    newCode = validPassword()
                    try: 
                        doorCd["Front Door"] = newCode
                    except TypeError:
                        speaker.say('There seems to be a problem on my system. I apologize. Please try again.')
                        speaker.runAndWait()
                        newCode = validPassword()
                        doorCd["Front Door"] = newCode
                                
                elif askUser == 3:
                    speaker.say("Input the new code for front door")
                    speaker.runAndWait()
                    
                    print(validPassword.__doc__)
                    newCode = validPassword()
                    try: 
                        doorCd["Front Door"] = newCode
                    except TypeError:
                        speaker.say('There seems to be a problem on my system. I apologize. Please try again.')
                        speaker.runAndWait()
                        newCode = validPassword()
                        doorCd["Front Door"] = newCode

                    speaker.say("Input the new code for back door")
                    speaker.runAndWait()

                    print(validPassword.__doc__)
                    newCode = validPassword()
                    try:
                        doorCd["Back Door"] = newCode
                    except TypeError:
                        speaker.say('There seems to be a problem on my system. I apologize. Please try again.')
                        speaker.runAndWait()
                        newCode = validPassword()
                        doorCd["Back Door"] = newCode
                
                elif askUser == 4:
                    justView = True
                    pass

                else:
                    speaker.say('Please choose among the available options.')
                    speaker.runAndWait()
                    time.sleep(1)
                    errorMenu = True
                    continue
                




                    #shud i add pa if magsame si codes for user to rethink 
                if justView == False:
                    time.sleep(1)
                    speaker.say('Password Valid. Saved!')
                    speaker.runAndWait()
                print('\nRemember your door codes:')
                for key, value in doorCd.items():
                    print(key + " : " + value)
                
                if justView == True:
                    speaker.say('Do you have second thoughts on your current codes?')
                    speaker.runAndWait()
                    time.sleep(1)
                    
                    doubts = input('Type Y/N\n').lower()

                    if 'y' in doubts:
                        errorMenu = True
                        continue
                    elif 'n' in doubts:
                        break
                        
                    else:
                        yesNo = ['y', 'n']
                        if not (yesNo[0] in doubts or yesNo[1] in doubts):
                            errorMenu = True
                            continue
                                                     
                break
        
                    
            #elif 'n' in onSecurity:

            else:
                speaker.say('That was confusing. Please clarify.')
                speaker.runAndWait()
                time.sleep(1)
                continue


def validPassword(): #designn temrinasdasds
    """These are the conditions need to be met:
    if its greater than 5 characters;
    if it has at least one lowercase letter;
    if it has at least one uppercase letter; and
    if it has at least one numeral; 
    """
    speaker.say("Evaluate if the input is valid as a password")
    speaker.runAndWait()
    
    inputValue = True
    if inputValue == True:
        time.sleep(2)
        password = str(input('Input: '))
        if not len(password): # JSHKSDF INPUT VALIDATION??hghgj
            time.sleep(1)
            speaker.say("Empty string was entered!")
            speaker.runAndWait()
            inputValue = False
        if len(password) < 5:
            print('The length of password should be greater than 5 characters.')    
            inputValue = False
        if not any(char.islower() for char in password): # determines if there is no letter in lowercase in 
            print('The password should have at least one lowercase letter.')  
            inputValue = False
        if not any(char.isupper() for char in password): # determines if there is no letter in uppercase 
            print('The password should have at least one uppercase letter.')  
            inputValue = False
        if not any(char.isdigit() for char in password): # determines if there is no digit 
            print('The password should have at least one numeral.')
            inputValue = False

        if inputValue == True:
            return str(password)

        elif inputValue == False:
            time.sleep(2)
            speaker.say('Invalid. Try again.')
            speaker.runAndWait()
            validPassword()


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
    security()

    #when inside change/code
    #music?
    #check business?



