import csv
import matplotlib.pyplot as plt

english_file = "english.csv"  #Insert the name for the CSV to be used for the stemming process
lyrics_file = "finaldata.csv"   #Insert the name for the CSV to be used for the lyrics data
iindex = {}        #Inverted index location to be saved


def stemming(word,english_file):
    """
    Takes a string word, and finds its stem in the file
    Returns the word if it is not present
    Returns the stem
    """
    #print("slow")
    word= word.lower()
    csv_reader = csv.reader(open(english_file))
    for line in csv_reader:
        if word in line:
            word = line[0]
            return word
    
    return word

def make_dict(lyrics_file,genreindexrange,authorindex,lyricindex):
    """
    Returns an inverted index of the file in the form:
    {lyric word: [artist, songname, genre]....} 
    """
    dict = {}
    counter = 0
    csv_reader = csv.reader(open(lyrics_file))
    for line in csv_reader:
        print(counter)
        counter +=1
        lyrics = line[lyricindex]
        genre = line[genreindexrange[0]:genreindexrange[1]]
        author = line[authorindex]
        cleanup = ""
        lyrics = lyrics.split("\n")
        lyrics = " ".join(lyrics)
        #print(lyrics)
        for letter in lyrics:
            if letter.isalpha():
                cleanup = cleanup + letter
            else:
               # print(letter)
                cleanup = cleanup + " "
        #print(cleanup)
        lyricslist = ""
        lyricslist = cleanup.split()
        for word in lyricslist:
            w = stemming(word,english_file)
            dict.setdefault(w,[])
            dict[w].append(author)
            for each in genre:
                dict[w].append(each)
        
    return dict

def find_word(word):
    """
    Find a given word/term in the iindex
    Returns the genres/songs in which it was found
    """
    pass

print(stemming("made",english_file))
print(stemming("fought",english_file))
print(stemming("walked",english_file))
print(stemming("ran",english_file))
d = make_dict(lyrics_file,(1,11),18,0)

for item in d:
    print(item, " : ",d[item])


#x_values = [0,1,2,3,4,5]
#squares = [0,1,4,9,16,25]
#plt.plot(x_values,squares)
#plt.show()