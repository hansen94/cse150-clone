# -*- coding: utf-8 -*-
__author__ = 'hdharmaw@ucsd.edu, A91413023, mdarmadi@ucsd.edu, A11410141, vcchandr@ucsd.edu, A12496582'


from assignment2 import Player, State, Action
import time


class EvaluationPlayer(Player):
    def move(self, state):
        """Calculates the best move after 1-step look-ahead with a simple
        evaluation function.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """

        # *You do not need to modify this method.*
        #t0 = time.time()
        best_value = -1.0

        actions = state.actions()
        if not actions:
            actions = [None]

        best_move = actions[0]
        for action in actions:
            result_state = state.result(action)
            value = self.evaluate(result_state, state.player_row)
            if value > best_value:
                best_value = value
                best_move = action
        #t1 = time.time()
        #print "Time: " + str(t1 -t0)
        # Return the move with the highest evaluation value
        return best_move

    def evaluate(self, state, my_row):
        """
        Evaluates the state for the player with the given row
        """

        goalStone = state.board[state.opponent_goal_idx]
        oppStones = state.board[state.player_goal_idx]
        stonesYourSide = 0
        stonesOppSide = 0
        m = float(state.M)
        n = float(state.N)

        oppRange = state.possible_action_range()
        for a in range(oppRange[0], oppRange[1]):
            stonesOppSide += state.board[a]

        if my_row == 0:
            for i in range(0, state.player_goal_idx):
                stonesYourSide += state.board[i]
        else:
            for i in range((state.player_goal_idx + 1), (state.opponent_goal_idx)):
                stonesYourSide += state.board[i]

        result = (1 / (2 * m * n)) * (goalStone - oppStones + stonesYourSide - stonesOppSide)

        return result
        # raise NotImplementedError("Need to implement this method")
