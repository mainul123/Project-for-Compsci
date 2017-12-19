import csv
import matplotlib.pyplot as plt
import numpy as np

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
    print("Generating iindex dictionary...")
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
    print("Done!")
    return dict

def stem_dict(unstemmed_dict):
    """
    Applies the stemming algorithm to the dictionary
    """
    d = {}
    print("Stemming the dictionary...")
    keyword = ""
    #count = 0
    #print(len(unstemmed_dict))
    for key in unstemmed_dict.keys():
        #print(count)
        #count += 1
        keyword = stemming(key,english_file)
        d.setdefault(keyword,[])
        d[keyword].append(unstemmed_dict[key])
        #if(key == 'shake'):
            #print(keyword, ": ", d[keyword])
    print("Done!")
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

#The purpose of the graph is to show the number of times a author associated with that “genre” uses “word” how many times 
    
def values_for_graph(iindex,authorindex,word):
    x_vals = [] #authors
    y_vals = [] #wordcount per author
    word = stemming(word,english_file)
    
    csv_reader = csv.reader(open(lyrics_file))
    print("Generating graph...")
    for line in csv_reader:
        authorname = line[authorindex]
        if authorname not in x_vals:
            x_vals.append(authorname)
    wordcount = 0
    for author in x_vals:
        wordcount = 0
        if word in iindex.keys():
                for l in iindex[word]:
                    #print(l.count('Taylor Swift'))
                    wordcount += l.count(author)
        y_vals.append(wordcount)
         
    i = 0
    while i < len(x_vals):
        print(x_vals[i], " : ",y_vals[i])
        i+=1
    
    #print(x_vals)
    #print(y_vals)
    print("Done!")
    plt.scatter(x_vals, y_vals, s = 5)
    titlestring = "Frequency of the word '" + word + "' vs. Author"
    plt.title(titlestring)    
    plt.xlabel("Authors",fontsize = 18)
    plt.ylabel("Frequency of word", fontsize = 18)
    plt.xticks(rotation=90)
    plt.show()

#print(stemming("made",english_file))
#print(stemming("fought",english_file))
#print(stemming("walked",english_file))
#print(stemming("ran",english_file))
d = make_dict(lyrics_file,(1,11),17,0)
#for item in d:
#    print(item, ":",d[item])
iindex = stem_dict(d)
#print(iindex)
#for item in iindex:
#    print(item, " : ",iindex[item])
inputword = input("Input a word, and a graph showing the number of occurences and the artists that used it will be made:  ")
inputword = inputword.lower()
values_for_graph(iindex,17,inputword)


#x_values = [0,1,2,3,4,5]
#squares = [0,1,4,9,16,25]
#plt.plot(x_values,squares)
#plt.show()
