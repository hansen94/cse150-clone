# -*- coding: utf-8 -*-

__author__ = 'hdharmaw@ucsd.edu, A91413023, mdarmadi@ucsd.edu, A11410141, vcchandr@ucsd.edu, A12496582'


from assignment2 import Player, State, Action
import sys


class CustomAgentPlayer(Player):
    """The custom player implementation.
    """

    DEPTH = 5 # customizable depth

    def __init__(self):
        """Called when the Player object is initialized. You can use this to
        store any persistent data you want to store for the  game.

        For technical people: make sure the objects are picklable. Otherwise
        it won't work under time limit.
        """

        # VARIABLES
        self.tTable = {} # transposition table
        self.aTable = {} # action transposition table


        pass

    def move(self, state):
        global DEPTH
        """
        You're free to implement the move(self, state) however you want. Be
        run time efficient and innovative.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """

        best_act = None
        best_v = -sys.maxint

        for d in range(1, DEPTH):
            actions = state.actions()
            best_act = actions[0]

            for action in actions:
                util = self.maxVal(state.result(action), d + 1, -sys.maxint, sys.maxint)
                self.aTable[action] = util


        raise NotImplementedError("Need to implement this method")


    def maxVal(self, state, depth, alpha, beta):
        global nextState

        if state.is_terminal():
            return state.utility(self)

        v = -sys.maxint

        if not state.actions():
            v = max(v, self.minVal(state.result(None), alpha, beta))
        else:
            for a in state.actions():
                v = max(v, self.minVal(state.result(a), alpha, beta))
                if v >= beta:
                    return v
                if (v > alpha):
                    nextState = a
                alpha = max(v, alpha)

        return v

    def minVal(self, state, depth, alpha, beta):
        global nextState

        if state.is_terminal():
            return state.utility(self)

        v = sys.maxint

        if not state.actions():
            v = min(v, self.maxVal(state.result(None), alpha, beta))
        else:
            for a in state.actions():
                v = min(v, self.maxVal(state.result(a), alpha, beta))
                if v <= alpha:
                    return v
                beta = min(v, beta)

        return v

