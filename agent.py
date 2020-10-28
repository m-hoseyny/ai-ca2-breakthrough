import random


# class AlphaBetaTree:
#     def __


class Agent:
    def __init__(self, color, oppopnentColor, time=None):
        self.color = color
        self.oppopnentColor = oppopnentColor

    def move(self, current_state, turn):
        """Use the minimax tree and the utility function to figure out the next
        move.

        rtype: a tuple, a string (in that order)
        """
        # Initialize a minimax tree.
        decisionTree = Minimax_Agent(current_state, turn, self.evasive_ustility)
        decisions = decisionTree.get_val()
        dest = decisions[0]        
        move_direction = decisions[1]

        return dest, move_direction



    def evasive_ustility(self, input_state):
        p_remaining = 0.  
        
        for row in input_state:		
            for column in row:			
                if self.color == "B":
                    if column == "B":
                        p_remaining += 1
                if self.color == "W":
                    if column == "W":
                        p_remaining += 1

        percentange = random.uniform(0,1)	
        Num = round(percentange , 2)		
        utility = p_remaining + Num        
        return utility