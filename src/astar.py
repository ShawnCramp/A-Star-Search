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
Initial Declarations -------------------------------------"""


def coordinates(map_handle):
    coords = [(i+1, j+1, c) for i, line in enumerate(open(map_handle))
             for j, c in enumerate(line[0:10])]
    
    for coord in coords:
        print(coord)
    
    print('coords')
    return coords


def astar():
    print('astar')
    

def branch():
    print('branch')


def main():
    map_handle = 'layoutmap.txt'
    coords = coordinates(map_handle)
    print('main')
    
    
""" Launch Main Program """
main()
