# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]


def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"

  from game import Directions

  # Initialization
  search_stack = util.Stack()
  traversed = []
  initial_state = problem.getStartState()

  # Push the starting state in the stack.
  search_stack.push((initial_state, []))

  # While search_stack in the fringe of the present state is not empty, go on searching the goal.
  while search_stack:
      (state, move_dir) = search_stack.pop()

      if not state in traversed:  # Avoid revisiting the same state.
          traversed.append(state)

          if problem.isGoalState(state):
              return move_dir  # Return move_dir if goal is searched.

          children = problem.getSuccessors(state)  # Get all child nodes of this state.

          for child in children:  # child[0]: state of child, child[1]: action to get to the child.
              search_stack.push((child[0], move_dir + [child[1]]))

  return []  # Goal does not exist in the search_stack.


def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"

  from game import Directions

  # Initialization
  search_queue = util.Queue()
  traversed = []
  initial_state = problem.getStartState()

  # Push the starting state in the queue.
  search_queue.push((initial_state, []))

  # While search_queue in the fringe of the present state is not empty, go on searching the goal.
  while search_queue:
      (state, move_dir) = search_queue.pop()

      if not state in traversed: # Avoid revisiting the same state.
          traversed.append(state)

          if problem.isGoalState(state):
              return move_dir  # Return move_dir if goal is searched.

          children = problem.getSuccessors(state) # Get all child nodes of this state.

          for child in children: # child[0]: state of child, child[1]: action to get to the child.
              search_queue.push((child[0], move_dir + [child[1]]))

  return [] # Goal does not exist in the search_queue.
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  search_pri_queue = util.PriorityQueue()
  traversed = []  # List of already visisted nodes
  #move_dir = []   # List of actions taken to get to the current node
  initial = problem.getStartState()  # Starting state of the problem

  # Push a tuple of the start state and blank action list onto the given
  # fringe data structure. If a priority queue is in use, then calculate
  # the priority using the heuristic

  search_pri_queue.push((initial, []), heuristic(initial, problem))

  # While there are still elements on the fringe, expand the value of each
  # node for the node to explore, actions to get there, and the cost. If the
  # node isn't traversed already, check to see if node is the goal. If no, then
  # add all of the node's successors onto the fringe (with relevant
  # information about path and cost associated with that node)
  while search_pri_queue:

      (node, actions) = search_pri_queue.pop()

      if not node in traversed:
          traversed.append(node)
          if problem.isGoalState(node):
              return actions
          children = problem.getSuccessors(node)
          for child in children:
              (coordinate, direction, cost) = child
              newActions = actions + [direction]
              newCost = problem.getCostOfActions(newActions) + heuristic(coordinate, problem)
              search_pri_queue.push((coordinate, newActions), newCost)

  return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch