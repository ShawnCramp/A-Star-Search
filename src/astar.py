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
    neighbours to each node
    """
    def __init__(self):
        self.edges = {}

    def neighbours(self, id):
        return self.edges[id]


def map_coordinates(map_handle):
    """
    Create Map object with all coordinates and neighbours

    :param map_handle:
    :return:
        Coordinates List
    """
    coords = [(i+1, j+1, c) for i, line in enumerate(open(map_handle))
             for j, c in enumerate(line[0:10])]
    
    for coord in coords:
        print(coord)
    
    print('Needs to be implemented with Map Object')
    return coords


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
    print('needs to be implemented')


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
        for node in coordinates.neighbours(current_node):
            print('temp')

    print('Needs to be finished')
    return found, cost


def main():
    """
    Main Loop of Program

    :return:
    """
    map_handle = 'layoutmap.txt'
    coordinates = map_coordinates(map_handle)

    rendevous = (4, 7)
    robot_one = (2, 1)

    print('main')
    
    
""" Launch Main Program """
main()
