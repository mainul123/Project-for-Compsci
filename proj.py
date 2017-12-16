import csv
english_file = "english.csv"  #Insert the name for the CSV to be used for the stemming process
lyrics_file = ""   #Insert the name for the CSV to be used for the lyrics data
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
    pass

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
