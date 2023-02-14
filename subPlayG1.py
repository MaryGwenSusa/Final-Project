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

# ask user if want some tunes
# need an initial list/array?

    # show lists: according to artist, song
    # shuffle based on year (actually arranging them)
    # group based on: genre, country

#when they are stored - create random index? based on song len 
#                       - get song of the index
# show that song playing with options of next or backwward or quit
#               show the next/or before song
# or quit

#del
#append

def header():
    title = "          VINYL PLAYER          "
    print("=" *  33) # created a header design
    print(title)
    print("=" * 33)

    for songtl, songInfo in songs.items():
        print(">", songtl, 'by', songInfo['Artist'])

header()





def artists():
    title = "          ARTISTS         "
    print("=" *  33) # created a header design
    print(title)
    print("=" * 33)

    for songInfo in songs.values():
        print(">", songInfo['Artist'])

artists()

def genre():
    title = "          GENRES         "
    print("=" *  33) # created a header design
    print(title)
    print("=" * 33)
    songGenre = []
    for songInfo in songs.values():
        songGenre = songInfo['Genre']
    
    print(songGenre)

genre()


def year():
    title = "          YEAR         "
    print("=" *  33) # created a header design
    print(title)
    print("=" * 33)

    for songInfo in songs.values():
        print(">", songInfo['Year'])




    

