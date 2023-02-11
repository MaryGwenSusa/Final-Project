import time

print("This is the front door!")
time.sleep(1)
print("Type in your password to unclock the door.")
time.sleep(0.5)

code = "0p3nd00R"
guesses = ''
turns = 3

#check if the turns are more than zero
while turns > 0:         
    failed = 0

    # for every character in code    
    for char in code:
        print ("_",end=""),     
        if guesses != code:    
            failed += 1

    if failed == 0:        
        print ("Unlocking...")
        time.sleep(1)
        print ("You may come in!")
        break
       
