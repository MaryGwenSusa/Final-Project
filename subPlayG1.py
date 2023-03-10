import pyttsx3
import time

songs = {
    "If I Had to Write a Song About You ð" : {
        'Artist': 'Aaron Taylor',
        'Genre': 'Indian Film Pop,R&B/Soul',
        'Year': '2016',
        'Country': 'International',
    },
    "Waffle Fries ð" : {
        'Artist': 'sunshine blvd.',
        'Genre': 'Pop',
        'Year': '2019',
        'Country': 'International',
    },
    "Solomon ð" : {
        'Artist': 'Munimuni, Clara Benin',
        'Genre': 'Indie Folk,Country',
        'Year': '2019',
        'Country': 'Local',
    },
    "Casual ð " : {
        'Artist': 'Jesse Barrera, Jeff Bernat, Johnny Stimson',
        'Genre': 'R&B/Soul',
        'Year': '2020',
        'Country': 'International',
    },
    "Ride ð" : {
        'Artist': 'HYBS',
        'Genre': 'Alternative/Indie,Pop',
        'Year': '2022',
        'Country': 'International',
    },
    "Absence of Youâï¸" : {
        'Artist': 'grentperez',
        'Genre': 'Alternative/Indie,Rock',
        'Year': '2022',
        'Country': 'International',
    },
    "Too Good ð¦" : {
        'Artist': 'Christian Kuria',
        'Genre': 'R&B/Soul',
        'Year': '2020',
        'Country': 'International',
    },
    "Still ð" : {
        'Artist': 'Jeff Bernat',
        'Genre': 'R&B/Soul',
        'Year': '2019',
        'Country': 'Local',
    },
    "Lemonade ð" : {
        'Artist': 'Jeremy Passion, Melissa Polinar, Gabe Bondoc',
        'Genre': 'Alternative/Indie',
        'Year': '2011',
        'Country': 'International',
    },
    "Used to Me ð­" : {
        'Artist': 'Luke Chiang',
        'Genre': 'Alternative/Indie,Pop',
        'Year': '2019',
        'Country': 'International',
    }
    
}


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data) #if self.left already has a value--recursively call the function to create another small subtree with another child value
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data) #if self.right already has a value--recursively call the function to create another small subtree with another child value
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        #returns the nodes in ascending order
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base/root node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

def build_tree(elements):
    #helper method - takes elements as inputs
    root = BinarySearchTreeNode(elements[0])

    for i in range (1, len(elements)):
        root.add_child(elements[i])
    
    return root


def header():
    title = "         ð½ \033[01m\033[36mVINYL PLAYER\033[0m ð½         "
    print("\033[0m=" *  36) # created a header design
    print(title)
    print("=" * 36)

    for songtl, songInfo in songs.items():
        print("ð¶ ", "\033[01m%s\033[0m" % songtl, '\033[3mby', "%s\033[0m" % songInfo['Artist'])


def allTracks():
    whenError = False
    if whenError == False:
        speaker.say("What do you want to do?")
        speaker.runAndWait()
        print('\n     \033[0m\033[33m\033[01m1\033[0m -> \033[3mPlay all\033[0m') 
        print('     \033[33m\033[01m2\033[0m -> \033[3mDive into subplaylists\033[0m')

    try:
        songMix = int(input("Choose a number:\033[32m ")) #user validation
    except ValueError:
        speaker.say('That was confusing. Choose again.')
        speaker.runAndWait()
        whenError = True
        allTracks()
    playing = 0
    while True:
        if playing == 2:
            songMix = 2
        if songMix == 1:
            speaker.say("Do you want to shuffle the playlist?")
            speaker.runAndWait()
            onShuffle = input("\033[0mType Y/N ð¤\n\033[32m").lower() 
            if 'y' in onShuffle:
                print('\n\033[0m\033[3m\033[95mShuffling...\033[0m') #design

                """temp = []
                songYrs = []
                for songtl, songInfo in songs.items():
                    temp.append(songtl)
                    songYrs.append(songInfo['Year'])

                toBeSorted = dict(zip(temp,songYrs))
                srtdDict = sorted(toBeSorted.items(), key=lambda x:x[1])
                print(srtdDict)
                elemNum = 0
                tempTup = []

                while len(tempTup) != len(srtdDict):
                    for e in srtdDict:
                        
                        print('Now Playing', e[0], '(' + e[1] + ') by', end=" ")
                        for i in songs.keys():
                            if i == e[0]:
                                
                                for songtl, songInfo in songs.items():
                                    if i == songtl:
                                        print(songInfo['Artist'])
                                        time.sleep(4)
                                        del e
                                        break
                                elemDel = srtdDict[elemNum]
                                tempTup.append(elemDel)
                                break"""

                elemNum = 0
                tempTup = []
                srtdDict = []
                srtdDict = sorted(songs.values(), key=lambda x:x.get('Year')) # sorts the dict using year key values
                index = 0
                while len(tempTup) != len(srtdDict):
                    for songtl, songInfo in songs.items():
                        if songInfo['Year'] == srtdDict[index]['Year']: # if songtl's year value is equal to the first element of srtDict list which is the oldest year (smallest in value)
                            print('\n\033[3mNow Playing\033[0m', "\033[01m%s\033[0m" % songtl, '\033[3m(' +  srtdDict[index]['Year'] + ') by', songInfo['Artist'] + '..\033[0m' ) # design
                            time.sleep(4)
                            elemDel = srtdDict[elemNum]
                            tempTup.append(elemDel) # append the srtDict element that has matched a value in the og dict to another list-- while loop will be false when all element matched to value in og dict
                            index+=1 #increment index of srtDict element (sorted in year)

                            if index == (len(srtdDict)): # since srtDict list will eventually become out of range if index of srtDict is equal to its length then break out on the for loop
                                break

            elif 'n' in onShuffle:
                for songtl, songInfo in songs.items():
                    print('\n\033[0m\033[3mNow Playing\033[0m', "\033[01m%s\033[0m" % songtl, '\033[3m('  +  songInfo['Year'] + ') by', songInfo['Artist'] + '..\033[0m') 
                    time.sleep(4)
            else:
                speaker.say('That was confusing. Please clarify.')
                speaker.runAndWait()
                continue

            listenAgain()

        elif songMix == 2:
            speaker.say('What are you in for?')
            speaker.runAndWait()
            print('\n \033[0m\033[34m\033[01m1\033[0m -> \033[3mFeeling a certain genre\033[0m') 
            print(' \033[34m\033[01m2\033[0m -> \033[3mWanna hear some local artists\033[0m')
            print(' \033[34m\033[01m3\033[0m -> \033[3mInto foreign music\033[0m')
            try:
                sub = int(input("Choose a number: \033[32m "))
            except ValueError:
                speaker.say('That was confusing. Please clarify.')
                speaker.runAndWait()
                playing = 1
                continue

            if sub == 1:
                genre()
            elif sub == 2:
                localInt(sub)
            elif sub == 3:
                localInt(sub)
            else:
                speaker.say('Please choose among the available options.')
                speaker.runAndWait()
                playing = 1
                continue
        else:
            speaker.say('Please choose among the available options.')
            speaker.runAndWait()
            allTracks()

def listenAgain():
    speaker.say('Listen more?')
    speaker.runAndWait()
    listen = input("\nType Y/N ð¤\n\033[32m").lower()
    if 'y' in listen:
        allTracks()
    elif 'n' in listen:
        speaker.say("Activate me if you'll need my help again.")
        speaker.runAndWait()
        print("\033[0m\nð¤ ð¤ ð¤")
        time.sleep(2)
        exit()
    else:
        speaker.say('That was confusing. Please clarify.')
        speaker.runAndWait()
        listenAgain()

def genre():
    speaker.say('Here are the list of genres of the records you own. Choose one.')
    speaker.runAndWait()
    title = "            \033[01m\033[36mGENRES\033[0m           "
    print("\033[0m=" *  30) # created a header design
    print(title)
    print("=" * 30)
    songGenre = []
    for songInfo in songs.values():
        songGenre.append(songInfo['Genre']) # append Genre values to another list but each will be appended as individual list
    
    splitted = []
    oneList = []
    firstIndex = 0
    for e in songGenre: # since nested list
        init = e.split(',') # since some songs encompasses different genres split them
        splitted.append(init)
        for i in splitted: 
            while len(i):
                oneList.append(i[firstIndex]) # inner list each element will be appended
                i.pop(0) # then pop from splitted list
                
    oneList = list(dict.fromkeys(oneList)) # fromkeys() is a built-in function that generates a dictionary from the keys you have specified.
    binaryUsage = build_tree(oneList)
    arranged = binaryUsage.in_order_traversal() # sorting them alphabetically
    for i in arranged: # sorted list
        firstIndex+=1
        print(' ', "\033[34m\033[01m%s\033[0m" % firstIndex, '->', "\033[01m%s\033[0m" % i)
    
    while True:
        try:
            chooseGenre = int(input('Choose a number: \033[32m ')) 
        except ValueError:
            speaker.say('That was confusing. Please clarify.')
            speaker.runAndWait()
            continue

        if chooseGenre > 0 and chooseGenre < 9:
            title = "                    "
            print(title,"%s\033[0m" % arranged[chooseGenre - 1].upper(), title) 
            for songtl, songInfo in songs.items():
                if arranged[chooseGenre - 1] in songInfo['Genre']:
                    print('\033[0m\033[3mNow Playing\033[0m', "\033[01m%s\033[0m" % songtl, '\033[3mby', songInfo['Artist'] + '..\033[0m')
                    time.sleep(4)
        else:
            speaker.say('Please choose among the available options.')
            speaker.runAndWait()
            continue
            
        listenAgain()

def localInt(pref):
    choices = ['Local', 'International']
    if pref > 1 and pref < 4:
        title = "                    "
        header = choices[pref - 2] 
        label = header + " Artist/s"
        print("\033[32m%s" % title, "\033[01m\033[36m%s\033[0m" % label.upper(), title)
        for songtl, songInfo in songs.items():
            if header in songInfo['Country']:
                print('\033[0m\033[3mNow Playing\033[0m', "\033[01m%s\033[0m" % songtl, '\033[3mby', songInfo['Artist'] + '..\033[0m')
                time.sleep(4)

        listenAgain()

def main ():

    header()
    allTracks()



speaker = pyttsx3.init() #initialize
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 155) #adjusted the speed of reading since its default 200 is too fast

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) #change voice for female through changing its index since default is male still male index is 0

main()







    



    

