from collections import deque
songs = {
    "If I Had to Write a Song About You" : {
        'Artist': 'Aaron Taylor',
        'Genre': 'Indian Film Pop, R&B/Soul',
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
        'Genre': 'Indie Folk, Country',
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
        'Genre': 'Alternative/Indie, Pop',
        'Year': '2022',
        'Country': 'International',
    },
    "Absence of You" : {
        'Artist': 'grentperez',
        'Genre': 'Alternative/Indie, Rock',
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
        'Genre': 'Alternative/Indie, Pop',
        'Year': '2019',
        'Country': 'International',
    }
}
def genre():
    # create subplaylist?
    # what genre are you in for
    # want some local tunes or international artists
    #speaker.say('That was confusing. Please clarify.')
    #speaker.runAndWait()
    title = "          GENRES         "
    print("=" *  33) # created a header design
    print(title)
    print("=" * 33)
    songGenre = []
    for songInfo in songs.values():
        songGenre.append(songInfo['Genre'])
    songGenre = list(set(songGenre))
    
    options = 1
    splitted = deque()
    for e in songGenre:
        init = e.split(' ')
        splitted.append(init)

        #print(options, '->', e)
        #options+=1
    print(splitted)
genre()

