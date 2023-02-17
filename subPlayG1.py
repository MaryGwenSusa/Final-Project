import pyttsx3
from collections import deque
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

    # show lists: according to artist, song
    # shuffle based on year (actually arranging them)
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

def header():
    title = "          VINYL PLAYER          "
    print("=" *  33) # created a header design
    print(title)
    print("=" * 33)

    for songtl, songInfo in songs.items():
        print("🎶", songtl, 'by', songInfo['Artist'])


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
            print(' 1 -> Feeling a certain Genre')
            print(' 2 -> Wanna hear some local artists')
            print(' 3 -> Into foreign music')
            sub = int(input("> "))
            if sub == 1:
                genre()
            elif sub == 2:
                pass
            elif sub == 3:
                pass
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
    # create subplaylist?
    # what genre are you in for
    # want some local tunes or international artists

    title = "          GENRES         "
    print("=" *  33) # created a header design
    print(title)
    print("=" * 33)
    songGenre = []
    for songInfo in songs.values():
        songGenre = songInfo['Genre']
    
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
    for i in oneList:
        firstIndex+=1
        print(' ', firstIndex, '->', i)


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





    



    

