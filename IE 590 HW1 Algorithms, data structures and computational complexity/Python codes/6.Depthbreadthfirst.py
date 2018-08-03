
graph = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"],
         "f": []
         }

def dfs_iter(graph, start, path=[]):
    """
    Iterative version of depth first search.
    Arguments:
        graph - a dictionary of lists that is your graph and who you're connected to.
        start - the node you wish to start at
        path - a list of already visited nodes for a path
    Returns:
        path - a list of strings that equal a valid path in the graph
    """
    q=[start]
    while q:
        v = q.pop()#extract the element when contained in stack
        if v not in path:#visit vertex if not visited
            path += [v]
            q += graph[v]
    return path

def bfs_iter(graph, start, path=[]):
    """
    Iterative version of breadth first search.
    Arguments:
        graph - a dictionary of lists that is your graph and who you're connected to.
        start - the node you wish to start at
        path - a list of already visited nodes for a path
    Returns:
        path - a list of strings that equal a valid path in the graph
    """
    q=[start]
    while q:
        v = q.pop(0)
        if not v in path:
            path +=[v]
            q += graph[v]
    return path
print("breadth first search path:",bfs_iter(graph,'a'))
print("depth first search path:",dfs_iter(graph,'a'))