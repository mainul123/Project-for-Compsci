english_file = ""  #Insert the name for the CSV to be used for tbe stemming process
lyrics_file = ""   #Insert the name for the CSV to be used for the lyrics data
iindex = {}        #Inverted index location to be saved


def stemming(word,english_file):
    """
    Takes a string word, and finds its stem in the file
    Returns the stem
    """
    pass

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
