"""
GuessCalc does math to narrow down guesses

Currently runs an O(n^2) search on a single guess on a 45,000 word dictionary file
"""

class GuessCalc():
    def __init__(self):
        pass


    # parameters:  filename    -> string
    # returns   :  wordList    -> list
    def loadWords(self, filename):
        print("Loading word list from file...")
        wordlist = list()
        with open(filename) as f:
            for line in f:
                wordlist.append(line.rstrip('\n'))
        return wordlist

    
    # make dict file only contain 5 letter words
    # TODO: write to new file and in future just load in pre cleaned dict file
    def thinHerd(self, dictionary):
        cleanList = list()
        for word in dictionary:
            if (len(word) == 5):
                cleanList.append(word)
        print(" ", len(cleanList), "words loaded.")
        print('\n'.join(cleanList))

        return cleanList


    # parameters:  guess       -> string
    #              dictList    -> list
    #              filename    -> string
    # returns   :  matches     -> list
    def calcGuess(self, guess, dictList, filename):
        print("Calculating guesses")
        wordList = loadWords(filename) 
        return wordList

