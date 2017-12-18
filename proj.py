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
    #counter = 0
    csv_reader = csv.reader(open(lyrics_file))
    for line in csv_reader:
        #print(counter)
        #counter +=1
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
            word = word.lower()
            dict.setdefault(word,[])
            dict[word].append(author)
            for each in genre:
                dict[word].append(each)
        
    return dict

def stem_dict(unstemmed_dict):
    """
    Applies the stemming algorithm to the dictionary
    """
    d = {}
    keyword = ""
    count = 0
    print(len(unstemmed_dict))
    for key in unstemmed_dict.keys():
        print(count)
        count += 1
        keyword = stemming(key,english_file)
        d.setdefault(keyword,[])
        d[keyword].append(unstemmed_dict[key])
        
    return d
##        if keyword != key: #Successfully found the word's stem
##            d.setdefault(keyword,[])
##            d[keyword].append(unstemmed_dict[key])
##        else:  #Word is a stem, or not common English
##            d.setdefault(key)
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
d = make_dict(lyrics_file,(1,11),17,0) 
iindex = stem_dict(d)
for item in iindex:
    print(item, " : ",iindex[item])
    
    
    
#The purpose of the graph is to show the number of times a author associated with that “genre” uses “word” how many times 
    
def values_for_graph(iindex,authorindex,word):
    x_vals = [] #authors
    y_vals = [] #wordcount per author
    csv_reader = csv.reader(open(lyrics_file))
    for line in csv_reader:
        authorname = line[authorindex]
        if authorname not in x_vals:
            x_vals.append(authorname)
    wordcount = 0
    for author in x_vals:
        if word in iindex.keys() and author in iindex[word]:
            wordcount = len(iindex[word])
     
    
    print(x_vals)
    print(wordcount)
    
values_for_graph(iindex,17,"make")
    
    
    
    



#x_values = [0,1,2,3,4,5]
#squares = [0,1,4,9,16,25]
#plt.plot(x_values,squares)
#plt.show()
