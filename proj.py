import csv
import matplotlib.pyplot as plt

english_file = "english.csv"  #Insert the name for the CSV to be used for the stemming process
lyrics_file = "#uncleaned.txt#"   #Insert the name for the CSV to be used for the lyrics data
iindex = {}        #Inverted index location to be saved


def stemming(word,english_file):
    """
    Takes a string word, and finds its stem in the file
    Returns the stem
    """
    word= word.lower()
    csv_reader = csv.reader(open(english_file))
    for line in csv_reader:
        if word in line:
            word = line[0]
    return word

def make_dict(lyrics_file):
    """
    Returns an inverted index of the file in the form:
    {lyric word: [artist, songname, genre]....} 
    """
    linemade =False
    line2made = False
    csv_reader = csv.reader(open(lyrics_file))
    for line in csv_reader:
        if linemade == False:
            print(line)
            linemade = True
        elif line2made == False:
            print(line)
            line2made = True
    return

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
make_dict(lyrics_file)

x_values = [0,1,2,3,4,5]
squares = [0,1,4,9,16,25]
plt.plot(x_values,squares)
plt.show()