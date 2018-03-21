# we'll use this list for or recursive DFS functions
Tree =  (1, 
        (2, None, (4, None, None)), 
        (3, (5, (7, None, None), (8, None, None)), 
        (6, (9, None, None), (10, (11, None, None), None)))   )

# we'll use this list for our iterative BFS function
Trees =  [1, 
        [2, None, [4, None, None]], 
        [3, [5, [7, None, None], [8, None, None]], 
        [6, [9, None, None], [10,[11, None, None], None]]]]


"""iterates through tree with a recursive algorithm via depth first search, and outputs all nodes"""
def dfs(tree, li = [] ):
    
    for i in tree:
        
        if isinstance(i, int):
            li.append(i)
        elif i == None:
            li.append(i)
        elif isinstance(i, tuple):
            dfs(tree = i, li = li)  
            
    return li

"""iterates through tree using a recursive algo via depth first search, and outputs all paths in a list
   We will use the output of this function to find all perfect binary child nodes in the path function below"""
def dfs_list(tree, path = []): 
    
    for i in tree:
        """if i is an int, append it to path inside of its own list"""
        if isinstance(i, int):
            path.append([i]) 
            """if i is none, it must be connected to an in, so append it to the last list
            that was appended"""
        elif i == None:
            """this if there is more than 2 Nones, the third None should be in the previous 
            list. This happens after 11, I think this is a mistake within the prescribed list"""
            if len(path[-1]) < 3:                
                path[-1].append(i)     
            else:
                path[-2].append(i)
                """if we get a tuple, rerun method, adding that tuple to the top of the stack"""        
        elif isinstance(i, tuple):
            dfs_list(tree = i, path = path)           
    return path

"""THIS TAKES OUTPUT OF DFS_LIST AS VECTORS ARGUMENT!!!!!!!!!"""            
"""gives the amount of nodes that have perfect subtrees. For example, in our example in the picture, there
   are 3 perfect binary subtrees of 3,3 and 7. So that would be our output"""
def path(vectors):
    indices = []
    scores = []
    parent = 0
    points = 0
    for e,i in enumerate(vectors):
        print('points',points)
        """if there is only one integer and no None types, we know there is 2 connecting
        nodes, these nodes are the only one we care about"""
        if len(i) == 1:
            """if parent == 0, this is the starting/parent node""" 
            if parent == 0:
                """add three points because we have three new perfect binary nodes"""
                points += 3
                """swithc parent to 1 so if we have another node with 2 children, we know its 
                not a parent node"""
                parent = 1
                """append the indice so we know the starting point for our perfect binary nodes"""
                indices.append(e)
                """if parent == 1, this is not a parent node, but still has 2 children"""
                print(points)
                """if the following also has two children, we need to check that node + 1 to see
                if that node also has 2 children, if it does, add 4 children"""
            elif parent == 1:
                for ii in vectors: 
                    if ii[0] == i[0] + 1:
                        if len(ii) == 1:
                            points += 4                       
                """if we get a node that has a None type, we dont care about it, but if our
                points are > 0, we need to log our points, than clear them back to 0"""
        elif points > 0:
            scores.append(points)
            points = 0
            parent = 0
    return scores
                    
            

"""iterates through tree with an iterative looping algorithm via breadth first search,
   and outputs all nodes in bfs order""" 
def bfs(queue):

    path = []
    
    while queue:
        
        for e,i in enumerate(queue):
            """if we get an integer here, append to the path than restart loop"""
            if isinstance(i,int):
                path.append(i)
                queue.pop(e)
                break
            
                """if we get a list, break the list down by a dimension by running it
                through another for loop, than append back to queue"""                     
            elif isinstance(i,list):
                for ii in i:
                    queue.append(ii)
                """pop the unbroken list down list that we oringally ran through for loop"""
                queue.pop(0) 
                """restart loop"""
                break
                """if i == None, pop None, then restart for loop""" 
            elif i == None:
                path.append(i)
                queue.pop(0)
                break   
    return path







    
