# CLASSES 

from typing import List
from xmlrpc.client import Boolean, boolean


class Problem():
    '''The abstract class for a formal problem. This will be subclassed and instanced to be solved via the various search algorithms'''

    def __init__(self, initial_state, goal_state = None):
        '''
        if there are no goal states, this is fine. Goal state can also be tweaked to be a condition against the state
        '''
        self.current_state = initial_state #initialize the current_state at initial
        self.goal_state = goal_state
        self.cost = 0 # initialize costs to be 0
    
    def actions(self, current_state) -> list:
        ''' 
        Returns a list of actions based on curren_state. Representation depends on the problem set. 
        Left blank for case-specific customization
        '''
        raise NotImplementedError
    
    def result(self, current_state, action) -> list:
        '''
        Returns a future state based on current state and the action upon it. 
        Representation depends on the problem set. 
        '''
        raise NotImplementedError
    
    def goal_test(self, current_state) -> bool: 
        '''
        Returns a boolean. True if goal is met
        '''
        if isinstance(self.goal_state, list): 
            return current_state in self.goal_state #DOUBLE CHECK WHAT THIS DOES 
        # else: 
        #     return current_state == self.goal_state
    
    def path_cost(self, cost, state1, action, state2) -> float:
        '''
        returns the cumulative cost, including the cost of new state transition
        '''
        #implement a cost calculator 
        return cost + 1 

    def value(self, state)

# LEARNING 
'''
CLARIFICATIONS 


'''

# DEBUGGING 

print ('hello world')
a = list('helloThere')
print (a)
print ('h' in a)