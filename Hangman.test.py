from getpass import getpass

class Hangman:

    body_parts = [ 'left leg', 'right leg', 'left arm', 'right arm', 'torso', 'head' ]
    body_parts_left = 6

    drawings = {
        6: '''
        ----|
        |   o 
        |  /|\\
        |   /\\
        ---------
        ''',
        5: '''
        ----|
        |   o
        |  /|\\
        |    \\
        ---------
        ''',
        4: '''
        ----|
        |   o
        |  /|\\
        |  
        ---------
        ''',
        3: '''
        ----|
        |   o
        |   |\\
        |
        ---------
        ''',
        2: '''
        ----|
        |   o
        |   |
        |
        ---------
        ''',
        1: '''
        ----|
        |   o
        |
        |
        ---------
        ''',
        0: '''
        ----|
        |
        |
        |
        ---------
        ''',
    }

    def remove_part ( self ):
        self.body_parts_left -= 1
        print( 'The HANGMAN lost a part! He lost his ' + self.body_parts[6-self.body_parts_left-1] + '...' )
        return self.body_parts_left

class Game:

    game_over = False
    hangman = Hangman()

    word = None
    progress = None
    guesses = None

    def set_word ( self, word ):
        self.word = [ char for char in word ]
        self.progress = [ '_' for char in word ]
        self.guesses = []

    
    def add_to_guesses ( self, letter ):
        self.guesses.append( letter )

    def print_event ( self, event ):
        events = {
            'correct' : 'Congrats! That letter is in the word.',
            'incorrect' : 'Sorry, that letter is not in the word.',
            'already guessed' : 'That letter has already been guessed.',
            'dead' : 'Your man has fallen. YOU\'VE LOST THE GAME.',
            'win' : 'Your man survived. YOU\'VE WON THE GAME!'
        }

        print( events[event] )

    def set_progress ( self, letter ):
        instances = [ index for index, char in enumerate(self.word) if char == letter ]
        for instance in instances:
            self.progress[instance] = letter

    def check_guess ( self, letter ):
        
        if letter not in self.guesses:

            self.add_to_guesses(letter)

            if letter in self.word:
                self.print_event('correct')
                self.set_progress(letter)
                
                print(self.progress)

                if '_' not in self.progress:
                    self.print_event('win')
                    self.game_over = True

            else:
                self.print_event('incorrect')
                self.hangman.remove_part()
                print ( self.hangman.drawings[self.hangman.body_parts_left] )

                if self.hangman.body_parts_left == 0:
                    self.print_event('dead')
                    self.game_over = True
        else:
            self.print_event('already guessed')
    
    def restart_game ( self, word ):
        self.hangman = Hangman()
        self.game_over = False
        self.set_word(word)

new_game = Game()
new_game.set_word( getpass('<player_1> Choose a word: ') )

while not new_game.game_over:
    letter = input('<player_2> Choose a letter: ')

    new_game.check_guess(letter)

    if ( new_game.game_over ):
        play_again = input('Would you like to play again? y/n ' )
        if play_again.lower() == 'y':

            new_game.restart_game( getpass('<player_1> Choose a word: ') )