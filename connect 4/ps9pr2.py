#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    """ a data type for a Connect Four's player
    """
    def __init__(self, checker):
        """constructs a new Player object by initializing checker and num_moves
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """returns a string representing a Player object, indicating which checker the player is using
        """
        s = 'Player ' + self.checker
        return s
    
    def opponent_checker(self):
        """returns a one-character string representing the checker of the Player object’s opponent. The method may assume that the calling Player object has a checker attribute that is either 'X' or 'O'.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """ returns the column where the player wants to make the next move.
        """
        i = int(input('Enter a column: '))
        while b.can_add_to(i) is False:
            print ('Try again!')
            i = int(input('Enter a column: '))
        self.num_moves += 1
        return i
            
            