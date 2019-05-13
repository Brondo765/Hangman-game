class Hangman():
    def __init__(self, word, right = '', wrong = ''):
        # create empty string attributes for string concatenation
        # uppercase the word upon initializing 
        self.word = str(word.upper())
        self.right = str(right)
        self.wrong = str(wrong)


    def getSecret(self):
        # used in playHangman() to return the word we set it at to guess
        self.getSecret = str(self.word)
        return self.getSecret
        
    def getHint(self):
        # create empty string here, every time it checks self.right
        # or self.wrong it creates a new instance of updated so
        # it looks like the is string mutable
        updated = ''
        for i in self.word:
            # add letter to updated in index location if guessed correctly
            if i in self.right:
                updated += i
            # otherwise place a '?' in place of letter slot not guessed
            elif i not in self.right:
                updated += '?'
                
        return updated

                                 
    def getRight(self):
        return self.right
                
    def getWrong(self):
        return self.wrong

    def getState(self, default = 'playing'):
        # default is 'playing' otherwise if conditions are met they win or lose
        self.default = default
        self.win = 'won'
        self.lose = 'lost'
        
        if self.getHint() == self.word:
            return self.win

        elif self.getHint() != self.word and len(self.wrong) >= 6:
            return self.lose
        
        elif self.getHint() != self.word and len(self.wrong) < 6:
            return self.default

    
    def guess(self, letter):
        # nested conditional for if they win that self.right doesn't get more
        # letters added to it after the game ends
        if letter.upper() in self.word and letter.upper() not in self.right:
            if self.getState() != self.lose:
                self.right += letter.upper()
                
        #same goes for here as above except if they lose the game self.wrong
        # doesn't have more letters added to it
        if letter.upper() not in self.word and letter.upper() not in self.wrong:
            if self.getState() != self.win and self.getState() != self.lose:
                self.wrong += letter.upper()
            


def playHangman(word):
    # create object and create loop until word guessed or 6 failed attempts 
    h = Hangman(word)
    while True:
        print("secret Word= '{}', correct= '{}', wrong= '{}'".format(h.getHint(), h.getRight(), h.getWrong()))
        letter = input('Guess a letter: ')
        h.guess(letter)
        
        if h.getState() == 'won':
            print('Congratulations, you guessed it! The word is {}.'.format(h.getSecret()))
            break
        
        elif h.getState() == 'lost':
            print('Sorry, you lose! The secret word is {}.'.format(h.getSecret()))
            break              

