# iterate_through_infinity
Iterate through a list of nodes where each dimension could theoretically be infinity. Here we take a look at utilizing recursive algorithms using DFS, and iterative algorithms using BFS. Take a look at the screen shot above, or click this link: 
[screenshot of binary tree](https://github.com/bnicholl/iterate_through_infinity/blob/master/Screen%20Shot%202018-03-07%20at%2012.57.28%20PM.png) This tree will be represented as a list that looks like this:                                         
Tree =                                                                                                                                  
        (1,                                                                                                                                                                                                                                                                        
        (2, None, (4, None, None)),                                                                                                     
        (3, (5, (7, None, None), (8, None, None)),                                                                                      
        (6, (9, None, None), (10, (11, None, None), None)))   )                                                                 
        
As you can see, any one of the dimensions in this tree could theoretically repersent a tree that is of infinite length. Some programmers have trouble understadning how to traverse a tree like this. For this repository, we are go over a few different ways to traverse this tree. One function is known a recursive algorithm, in which case we are going to traverse the tree using a depth first search method. The next is an iteative method using a loop. For this method we are going to use a breadth first search method. 
We are also going to go ahead and use the output from one of our DFS functions and write another function that finds all of the perfect subtrees in our Tree Variable, and output the number of nodes that are in the perfect subtree. If you look at our screen shot again, you will see there is 3 differnet positions where there is 3 perfect subtrees. One is at node locations [1,2,3], another at node location [6,9,10], and the third and biggest perfect subtree at node locations [3,5,6,7,8,9,10]. I documented each step in the algorthm so you can understand how my logic was broken down!  
