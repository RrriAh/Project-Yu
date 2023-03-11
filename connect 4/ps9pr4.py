#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer (Player):
    """a data type for a Connect Four's intelligent computer player, inheriting from Player
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object with checker, tiebreak, and lookahead
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)    
        super().__init__(checker)
        self. tiebreak = tiebreak
        self. lookahead = lookahead
    
    def __repr__(self):
        """ Returns a string that represents an AIPlayer object.
        """
        s = super().__repr__() + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s
    
    def max_score_column(self, scores):
        """ returns the index of the column with the maximum score. 
            scores: list
        """
        col = 0
        max_num = max(scores)
        choices = []
        for i in scores:
            if i == max_num:
                choices += [col]
            col += 1
        if self.tiebreak == 'LEFT':
            return choices[0]
        elif self.tiebreak == 'RIGHT':
            return choices[-1]
        else:
            return choices[random.choice(range(len(choices)))]
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s scores for the columns in b
            return a list containing one score for each column.
        """
        score_list = [50]*b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                score_list[col] = -1
            elif b.is_win_for(self.checker):
                score_list[col] = 100
            elif b.is_win_for(self.opponent_checker()):
                score_list[col] = 0
            elif self.lookahead == 0:
                score_list[col] = 50
            else:
                b.add_checker(self.checker,col)
                oppo = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                score_oppo = oppo.scores_for(b)
                max_oppo = max(score_oppo)
                score_list[col] = 100 - max_oppo
                b.remove_checker(col)
                
        return score_list            
                
    
    def next_move(self, b):
        """ return the called AIPlayer‘s judgment of its best possible move
        """
        scores = self.scores_for(b)
        choice = self.max_score_column(scores)
        self.num_moves += 1
        return choice
    
            
    