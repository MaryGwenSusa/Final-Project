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

def genre():
    # create subplaylist?
    # what genre are you in for
    # want some local tunes or international artists

    title = "          GENRES         "
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
    
    chooseGenre = int(input('> '))
    if chooseGenre > 0 and chooseGenre < 8:
        title = "                    "
        print(title, arranged[chooseGenre - 1].upper(), title)
        for songtl, songInfo in songs.items():
            if arranged[chooseGenre - 1] in songInfo['Genre']:
                print("Now Playing", songtl, 'by', songInfo['Artist'] + '..')
                time.sleep(4)


#📇 8 🔖 📄
    
genre()

