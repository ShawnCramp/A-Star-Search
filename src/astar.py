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
import operator


class Map:
    """
    Map object for holding all nodes in the map, as well as
    children to each node
    """
    def __init__(self, width, height, rendezvous, robots, node_dict):
        self.width = width
        self.height = height
        self.rendezvous = rendezvous
        self.robots = robots
        self.nodes = node_dict

    def children(self, node):
        return self.nodes[node]


def valid_coordinate(node_set, x, y, shift):
    """
    Check if node at node_set[x][y] is a valid node for robots
    to travel.

    :param node_set:
    :param x:
    :param y:
    :return:
    """
    valid = False
    new_x = x + shift[0]
    new_y = y + shift[1]
    
    print('x: {} y: {}'.format(x,y))
    print('shift: {}'.format(shift))
    print('new x: {} new y: {}'.format(new_x, new_y))
    
    
    if new_x >= 0 and new_x < len(node_set):
        if new_y >= 0 and new_y < len(node_set[0]):
            if node_set[new_x][new_y] == 0:
                valid = True
                print('Passed')
            else:
                print('Failed')
        else:
            print('Failed')
    else:
        print('Failed')
    print('-'*9)
    return valid


def get_children(node_set, x, y):
    """
    Using 2D list of all nodes in the map and an x and y coordinate
    in the map.  Get the child nodes attached to the x and y
    coordinate parameter.

    :param list:
        2D array of all nodes in the map
    :param x:
        x coordinate of current node
    :param y:
        y coordinate of current node
    :return children:
        dictionary of key node and children
    """
    temp = []
    neighbours = ((1, 0), (0, 1), (-1, 0), (0, -1))

    for shift in neighbours:
        #  check = node_set[x + value[0]][y + value[1]]
        if valid_coordinate(node_set, x, y, shift):
            temp.append((x + shift[0], y + shift[1]))
            #  print(temp)

    children = {(x, y): temp}
    print('children: {}'.format(children))
    print('-'*9)
    return children


def build_dictionary(node_set):
    """
    Build the dictionary of valid nodes and their explorable children.

    :param node_set:
    :return:
    """
    nodes = {}

    for x, x_line in enumerate(node_set):
        print('-'*9)
        print('x line: {} '.format(x_line))
        print('-'*9)
        for y, y_line in enumerate(x_line):
            if node_set[x][y] == 0:
                #  print(node_set[x][y])
                children = get_children(node_set, x, y)
                nodes.update(children)

    return nodes


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
    
    ''' Initial Declarations.  These will be overwritten '''
    node_dict = {}
    width = 0
    height = 0
    rendezvous = (0, 0)

    ''' 2D Array to initialize nodes '''
    temp = []
    
    ''' Build Map Object '''
    for i, line in enumerate(open(map_handle)):
        
        if i == 0:  # when i is 0
            line = line.strip().split(" ")
            width = line[0]
            height = line[1]
            
        elif i == 1:  # when i is 1
            line = line.strip().split(" ")
            robot_count = int(line[0])
            
        elif i - 2 < robot_count:
            robots.append(tuple(map(int, line.strip().split(" "))))
            
        elif i == 2 + robot_count:
            rendezvous = tuple(map(int, line.strip().split(" ")))
            
        else:
            temp.append(map(int, line.strip()))

    node_dict = build_dictionary(temp)

    return Map(width, height, rendezvous, robots, node_dict)


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


def a_star(coordinates, robot, rendezvous):
    """
    Complete A* Search Algorithm.

    :param coordinates:
        Map Coordinates Object
    :param rendezvous:
        Where the Robots meet.  (Ending Node Node)
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
    frontier.put(robot, cost)

    ''' Initial Dictionaries '''
    came_from = {}
    cost_so_far = {}
    came_from[robot] = None
    cost_so_far[robot] = 0

    ''' Loop through Queue '''
    while not frontier.empty():
        current_node = frontier.get()

        ''' If current node is robot node,
        break and return true -------- '''
        if current_node == rendezvous:
            break

        ''' Evaluate neighbouring nodes to current node '''
        for node in coordinates.children(current_node):
            print('Current: {}'.format(current_node))
            print('Currently Evaling Child: {}'.format(node))
            new_cost = cost_so_far[current_node] + 1

            if node not in cost_so_far or new_cost < cost_so_far[node]:
                print('If Check: Passed')

                cost_so_far[node] = new_cost
                priority = new_cost + heuristic(rendezvous, node)
                frontier.put(node, priority)

                print('Node Priority: {}'.format(priority))
                print('Frontier Size: {}'.format(frontier.qsize()))

                came_from[node] = current_node
                print('-'*9)
            else:
                print('If Check: Failed')
                print('Frontier Size: {}'.format(frontier.qsize()))
                print('-'*9)

    return came_from, cost_so_far


def pretty(d, indent=0):
    """
    Print Dictionary to console in a readable fashion

    :param d:
        Dictionary to print
    :param indent:
    :return:
    """
    for key, value in d.iteritems():
        print '\t' * indent + str(key)
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print '\t' * (indent+1) + str(value)


def main():
    """
    Main Loop of Program

    :return:
    """
    
    ''' Create Map Object '''
    map_handle = 'layoutmap2.txt'
    # map_structure = map_coordinates(map_handle)
    
    ''' 2D Array of nodes in Map '''
    # coords = [(i+1, j+1, c) for i, line in enumerate(open(map_handle)) for j, c in enumerate(line[0:10])]
    
    for i, line in enumerate(open(map_handle)):
        if i >= 5:
            print(line)
            
    print('testing')
    node_map = map_coordinates(map_handle)
       
    print('-'*18)
    print('mapping data: \n')
    print('width: {}'.format(node_map.width))
    print('height: {}'.format(node_map.height))
    print('rendezvous: {}'.format(node_map.rendezvous))
    print('robots: {}'.format(node_map.robots))
    print('dictionary:')
    pretty(node_map.nodes)

    test_node = (2, 0)
    print('\nChild Example: {}: {}'.format(test_node, node_map.children(test_node)))

    print('-'*18)
    print('Robot being Evaluated: {}'.format(node_map.robots[0]))
    print('Rendezvous Node: {}'.format(node_map.rendezvous))
    print('-'*40)
    print('Performing A* Search...')
    print('-'*40)
    came_from, cost_so_far = a_star(node_map, node_map.robots[0], node_map.rendezvous)
    print('-'*40)
    print('A* Complete...')
    print('Robot being Evaluated: {}'.format(node_map.robots[0]))
    print('Rendezvous Node: {}'.format(node_map.rendezvous))
    print('-'*40)
    # came_from, cost_so_far = a_star(node_map.nodes, (2, 1), (4, 7))
    print('Travelled Nodes: ')
    print(came_from)
    print('Evaluated Nodes ( Integer value is cost to get there ): ')
    print(cost_so_far)

    print('-'*18)
    total = 0
    for k, c in cost_so_far:
        total += c
    print('Total Cost of Steps Travelled: {}'.format(total))
    print('Cost to get to rendezvous Node: {}'.format(cost_so_far[node_map.rendezvous]))

    print('-'*18)
    sorted_dict = sorted(cost_so_far.items(), key=operator.itemgetter(1))
    print('Sorted Dictionary:')
    print(sorted_dict)
    

""" Launch Main Program """
main()
