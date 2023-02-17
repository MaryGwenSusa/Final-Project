import pyttsx3
import time

songs = {
    "If I Had to Write a Song About You" : {
        'Artist': 'Aaron Taylor',
        'Genre': 'Indian Film Pop,R&B/Soul',
        'Year': '2016',
        'Country': 'International',
    },
    "Waffle Fries" : {
        'Artist': 'sunshine blvd.',
        'Genre': 'Pop',
        'Year': '2019',
        'Country': 'International',
    },
    "Solomon" : {
        'Artist': 'Munimuni, Clara Benin',
        'Genre': 'Indie Folk,Country',
        'Year': '2019',
        'Country': 'Local',
    },
    "Casual" : {
        'Artist': 'Jesse Barrera, Jeff Bernat, Johnny Stimson',
        'Genre': 'R&B/Soul',
        'Year': '2020',
        'Country': 'International',
    },
    "Ride" : {
        'Artist': 'HYBS',
        'Genre': 'Alternative/Indie,Pop',
        'Year': '2022',
        'Country': 'International',
    },
    "Absence of You" : {
        'Artist': 'grentperez',
        'Genre': 'Alternative/Indie,Rock',
        'Year': '2022',
        'Country': 'International',
    },
    "Too Good" : {
        'Artist': 'Christian Kuria',
        'Genre': 'R&B/Soul',
        'Year': '2020',
        'Country': 'International',
    },
    "Still" : {
        'Artist': 'Jeff Bernat',
        'Genre': 'R&B/Soul',
        'Year': '2019',
        'Country': 'Local',
    },
    "Lemonade" : {
        'Artist': 'Jeremy Passion, Melissa Polinar, Gabe Bondoc',
        'Genre': 'Alternative/Indie',
        'Year': '2011',
        'Country': 'International',
    },
    "Used to Me" : {
        'Artist': 'Luke Chiang',
        'Genre': 'Alternative/Indie,Pop',
        'Year': '2019',
        'Country': 'International',
    }
}

# ask user if want some tunes
# need an initial list/array?

    # show lists: according to artist, song !!!
    # shuffle based on year (actually arranging them) !!!
    # group based on: genre, country
    #genre
    #when they are stored - create random index? based on song len 
    #                       - get song of the index

# show that song playing with options of next or backwward or quit
#               show the next/or before song
# or quit

#del
#append

speaker = pyttsx3.init() #initialize
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 155) #adjusted the speed of reading since its default 200 is too fast

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) #change voice for female through changing its index since default is male still male index is 0

#.popleft()


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
    title = "          VINYL PLAYER          "
    print("=" *  33) # created a header design
    print(title)
    print("=" * 33)

    for songtl, songInfo in songs.items():
        print("🎶 ", songtl, 'by', songInfo['Artist'])


def allTracks():
    speaker.say("What do you want to do?")
    speaker.runAndWait()
    print('\n     1 -> Play All') #shuffle, use year, or provide random index
    print('     2 -> Dive into subplaylist') #genre, local international
    songMix = int(input("> ")) #user validation
    while True:
        if songMix == 1:
            speaker.say("Do you want to shuffle the playlist?")
            speaker.runAndWait()
            onShuffle = input("Type Y/N\n ").lower()    
            if 'y' in onShuffle:
                print('Shuffling...')

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
                srtdDict = sorted(songs.values(), key=lambda x:x.get('Year'))
                index = 0
                while len(tempTup) != len(srtdDict):
                    for songtl, songInfo in songs.items():
                        if songInfo['Year'] == srtdDict[index]['Year']:
                            print('Now Playing', songtl, '(' +  srtdDict[index]['Year'] + ') by', songInfo['Artist'] + '..' )
                            time.sleep(4)
                            elemDel = srtdDict[elemNum]
                            tempTup.append(elemDel)
                            index+=1

                            if index == len(srtdDict):
                                break
            elif 'n' in onShuffle:
                for songtl, songInfo in songs.items():
                    print("Now Playing", songtl, '(' +  songInfo['Year'] + ') by', songInfo['Artist'] + '..')
                    time.sleep(4)
            else:
                speaker.say('That was confusing. Please clarify.')
                speaker.runAndWait()
                continue

            listenAgain()

        elif songMix == 2:
            speaker.say('What are you in for?')
            speaker.runAndWait()
            print('\n 1 -> Feeling a certain Genre')
            print(' 2 -> Wanna hear some local artists')
            print(' 3 -> Into foreign music')
            sub = int(input("> "))
            if sub == 1:
                genre()
            elif sub == 2:
                localInt(sub)
            elif sub == 3:
                localInt(sub)
            else:

                pass

def listenAgain():
    speaker.say('Listen more?')
    speaker.runAndWait()
    listen = input("Type Y/N\n ").lower()
    if 'y' in listen:
        allTracks()
    elif 'n' in listen:
        # diff feature or quit
        pass
    else:
        speaker.say('That was confusing. Please clarify.')
        speaker.runAndWait()
        listenAgain()

def genre():
    speaker.say('Here are the list of genres of the records you own. Choose one.')
    speaker.runAndWait()
    title = "            GENRES           "
    print("=" *  30) # created a header design
    print(title)
    print("=" * 30)
    songGenre = []
    for songInfo in songs.values():
        songGenre.append(songInfo['Genre'])
    
    splitted = []
    oneList = []
    firstIndex = 0
    for e in songGenre:
        init = e.split(',')
        splitted.append(init)
        for i in splitted:
            while len(i):
                oneList.append(i[firstIndex])
                i.pop(0)
                
    oneList = list(dict.fromkeys(oneList))
    binaryUsage = build_tree(oneList)
    arranged = binaryUsage.in_order_traversal()
    for i in arranged:
        firstIndex+=1
        print(' ', firstIndex, '->', i)
    
    while True:
        chooseGenre = int(input('> ')) #user validation
        if chooseGenre > 0 and chooseGenre < 8:
            title = "                    "
            print(title, arranged[chooseGenre - 1].upper(), title)
            for songtl, songInfo in songs.items():
                if arranged[chooseGenre - 1] in songInfo['Genre']:
                    print("Now Playing", songtl, 'by', songInfo['Artist'] + '..')
                    time.sleep(4)
                else:
                    speaker.say('That was confusing. Please clarify.')
                    speaker.runAndWait()
                    continue
            
        listenAgain()

def localInt(pref):
    choices = ['Local', 'International']
    if pref > 1 and pref < 4:
        title = "                    "
        header = choices[pref - 2] 
        label = header + " Artist/s"
        print(title, label.upper(), title)
        for songtl, songInfo in songs.items():
            if header in songInfo['Country']:
                print("Now Playing", songtl, 'by', songInfo['Artist'] + '..')
                time.sleep(4)

        listenAgain()
        





# option of adding a song?     

header()
allTracks()

    #for i, j in srtdDict():
    #for i in temp():
        #print('Now playing', srtdDict[i][j])
        #time.sleep(5)
    
    

    #for songInfo in songs.values():
        #songYrs.append(songInfo['Year'])
    #nodups = list(dict.fromkeys(songYrs)) # fromkeys() is a built-in function that generates a dictionary from the keys you have specified.
    #bubbleSort(nodups)
    #for songtl, songInfo in songs.items():
        #if songInfo['Year']: #acc useless
            #for e in nodups:
                #if songInfo['Year'] != e:
                    #again = e
                #if s
                 #songYrs.popleft()
                  #songYrs.append(songtl)

    #for songtl, songInfo in srtdDict.items():
        #print("🎶", songtl, ':', songInfo['Year'])

    #for new in songYrs:
        #print('Now Playing', new)
        

    

    #songYrs = deque()
    #for songInfo in songs.values():
     #   songYrs.append(songInfo['Year'])
    #nodups = list(dict.fromkeys(songYrs)) # fromkeys() is a built-in function that generates a dictionary from the keys you have specified.
    #for e in nodups:
        #print("⭐", e)

#def artists():
 #   title = "          ARTISTS         "
  #  print("=" *  33) # created a header design
   # print(title)
    #print("=" * 33)

    #for songInfo in songs.values():
     #   print(">", songInfo['Artist'])

#artists()





    



    

