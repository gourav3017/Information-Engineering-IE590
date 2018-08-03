import sys
from collections import defaultdict

def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # we've found our end node, now find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]
    # detect if it's the first time through, set current distance to zero
    if not visited: distances[start]=0
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxsize)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,sys.maxsize)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
    return shortestpath(graph,closestnode,end,visited,distances,predecessors)

if __name__ == "__main__":
    '''
    graph = {'a': {'b': 1},
            'b': {},
            'c': {},
            'd': {'e': 1},
            'e': {'d': 1},
            'f': {}}
    '''
    graph = {"a": {"c":5},
             "b": {"c":6, "e":8},
             "c": {"a":12, "b":5, "d":2, "e":1},
             "d": {"c":3},
             "e": {"c":24, "b":5},
             "f": {}
             }
    print(shortestpath(graph,'a','e'))

