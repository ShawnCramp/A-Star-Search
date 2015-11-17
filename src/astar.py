"""
-------------------------------------------------------------
Author: Shawn Cramp
ID: 111007290
Author: Edward Huang
ID: 100949380
Author: Bruno Salapic
ID: 100574460

Description: CP468 Final Assignment
Date: November, 13th, 2015
-------------------------------------------------------------
Assignment Task:

The purpose of this CP468 term project is to design and implement an 
A*-based algorithm to solve a path planning problem. You can use
 the programming language of your choice
 
Consider a Museum room that is patrolled by N robots at night.
At a pre-determined time, the robots are supposed to rendezvous
at a given point R in the room. The robots move inside the room,
and the room contains obstacles, such as chairs and benches for
the visitors, paintings, sculptures etc. The robots are supposed
to know the locations of the obstacles in the room. Implement an
A*-based algorithm to compute the path of each robot, from its
initial position to the given rendezvous point R.
-------------------------------------------------------------
Import Declarations --------------------------------------"""
from Queue import PriorityQueue


class Map:
    """
    Map object for holding all nodes in the map, as well as
    children to each node
    """
    def __init__(self, width, height, rendevous):
        self.width = width
        self.height = height
        self.rendevous = rendevous
        self.robots = []
        
        self.nodes = {}

    def children(self, node):
        return self.nodes[node]


def map_coordinates(map_handle):
    """
    Create Map object with all coordinates and neighbours

    :param map_handle:
        File handle for Map
    :return:
        Coordinates List
    """
    
    
    
    ''' List of Robots '''
    robots = []
    
    ''' Floor Coordinates '''
    nodes = {}
    
    ''' Build Map Object '''
    for i, line in enumerate(open(map_handle)):
        
        if i == 0: # when i is 0
            line = line.strip().split(" ")
            width = line[0]
            height = line[1]
            
        elif i == 1: # when i is 1
            line = line.strip().split(" ")
            robot_count = int(line[0])
            
        elif i - 2 < robot_count:
            robots.append(line.strip().split(" "))
            
        elif i == 2 + robot_count:
            rendevous = line.strip().split(" ")
            
        else:
            print(line)
            
    
    
    return i


def heuristic(g, h):
    """
    A* Heuristic
    f(n) = g(n) + h(n)

    :param g:
        Cost to reach node from start
    :param h:
        Estimated cost to get from n to goal
    :return f(n):
        Estimated total cost of cheapest
        solution through n
    """
    (g1, h1) = g
    (g2, h2) = h
    return abs(g1 - g2) + abs(h1 - h2)


def a_star(coordinates, rendezvous, robot):
    """
    Complete A* Search Algorithm.

    :param coordinates:
        Map Coordinates Object
    :param rendezvous:
        Where the Robots meet.  (Start Node)
        Eg. (5, 7)
    :param robot:
        Location of Robot.
        Eg. (2, 1)
    :return found:
        True if Robot is found, else False.
    :return cost:
        Cost of Path to Robot
    """

    ''' Cost of Initial Node '''
    cost = 0

    ''' Robot found boolean '''
    found = False

    ''' Priority Queue for evaluating locations '''
    frontier = PriorityQueue()

    ''' Put Root node into Queue '''
    frontier.put(rendezvous, cost)

    ''' Loop through Queue '''
    while not frontier.empty():
        current_node = frontier.get()

        ''' If current node is robot node,
        break and return true -------- '''
        if current_node == robot:
            break

        ''' Evaluate neighbouring nodes to current node '''
        for node in coordinates.children(current_node):
            
            print('temp')

    print('Needs to be finished')
    return found, cost


def main():
    """
    Main Loop of Program

    :return:
    """
    
    ''' Create Map Object '''
    map_handle = 'layoutmap.txt'
    # map_structure = map_coordinates(map_handle)
    
    ''' 2D Array of nodes in Map '''
    # coords = [(i+1, j+1, c) for i, line in enumerate(open(map_handle)) for j, c in enumerate(line[0:10])]
    
    for i, line in enumerate(open(map_handle)):
        if i >= 5:
            print(line)
            
    print('testing')
    map_coordinates(map_handle)
    


    tiles = {}
    
    item = {(1, 1): 'apple'}
    tiles.update(item)
    print(tiles[(1, 1)])
    
    

    print('main')
    
    
""" Launch Main Program """
main()
