'''
Created on Dec 14, 2012

@author: mama
Later add some login approvals to access the graph.
Make a graph reading the traffic named file which contains all the nodes and corresponding node connection relations. 
    '''
def getdata():
    graph = {'a': {'w': 14, 'x': 7, 'y': 9},
            'b': {'w': 9, 'z': 6},
            'w': {'a': 14, 'b': 9, 'y': 2},
            'x': {'a': 7, 'y': 10, 'z': 15},
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
            'z': {'b': 6, 'x': 15, 'y': 11}}
    return graph
