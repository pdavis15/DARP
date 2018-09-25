from random import*
import itertools
import copy
from math import factorial

#Python program to print topological sorting of a DAG
from collections import defaultdict
 

class Stack :
    '''Python implementation the stack'''
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
        
    def push(self,item):
        self.items.append(item)     
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

class Vertex :
    def __init__(self):
        self.distance
    '''Vertex to add in graph and keep track of distances'''
#Class to represent a graph
class Graph :
    def __init__(self,numVertices, graph=defaultdict(list)):
        self.graph = graph #dictionary containing adjacency List
        self.V = numVertices #No. of vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u-1].append(v-1)

    def deleteEdge(self,u,v):
        self.graph[u].remove(v)

    def __str__(self):
        s = ""
        for i in range(self.V):
            s += str(i)+":"+str(self.graph[i])+"\n"
        return s

    def printEdges(self):
        for i in range(self.V):
            print("vertex "+ str(i+1) +" is adjacent to: ")
            for neighbor in self.graph[i]:
                 print(neighbor+1)

    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and 
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbors
        # if any neighbor is visited and in 
        # recStack then graph is cyclic
        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor, visited, recStack) == True:
                    return True
            elif recStack[neighbor] == True:
                return True
 
        # The node needs to be poped from 
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self,v,visited,listt):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,listt)
 
        # Push current vertex to stack which stores result
        listt.insert(0,v)
 
    # The function to do Topological Sort. It uses recursive 
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        listt =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,listt)
 
        # Print contents of the stack
        #print (listt)
        return listt

    def findLongestPath(self):
        sortedGraph = self.topologicalSort()
        #print(sortedGraph)
        maxPathLength=0
        maxPath = []
        for k in range(self.V): #for every node in the graph find the longest path to all other nodes
            distance = [-99999999 for j in range(self.V)]#initialize distances to all nodes to be large negative
            longestPath=[[]for j in range(self.V)]
            distance[k]=0 #initialize distance of start node to 0
            longestPath[k]=[k]
            #print(k,longestPath[k])
            for i in range (self.V):
                v = sortedGraph[i]#sortedGraph[i] is the ith vertex in the topological ordering
                print("sorted graph",v)
                for j in self.graph[i]:
                    if i==j:
                        pass
                    else:
                        if (distance[j]<distance[i]+1):
                            distance[j]=distance[i]+1
                            #print(longestPath,i,j)
                            #print("before j: ",longestPath[j])
                            #print("before v: ",longestPath[v])
                            longestPath[j]= list(longestPath[v])
                            longestPath[j].append(j)
                            #print("longest path j: ",longestPath[j])
                            #print("longest path v: ",longestPath[v])
                        if (len(maxPath)<distance[j]):
                          #  print(longestPath[j])
                           # print(j,longestPath)
                            #print("before: ",maxPath)
                            maxPath = list(longestPath[j])
                            #print("after", maxPath)
        return maxPath




def generateRequestGraphs(timeLimit, numberOfNodes):
    '''This method will create every possible directed graph with the given number of nodes'''

    locations = []
    lengths = []
    #first just get a list of numbers for the locations
    for i in range(numberOfNodes):
        locations.append(i+1)
    #find all the permutations of 2 of these locations to get all the possible edges 
    possibleRequests = list(itertools.permutations(locations,2))
    possibleEdgePermutations=[]
    #find all the permutations/combinations of all of these edges to get the possible graphs.
    for i in range(numberOfNodes):
        possibleEdgePermutations.append(list(itertools.combinations(possibleRequests,i+1)))
        lengths.append(len(list(itertools.combinations(possibleRequests,i+1))))
    #turn this list of tuples into graph objects
    a= factorial(numberOfNodes)/ factorial(numberOfNodes-2)
    print(a)
    b=0
    for i in range(numberOfNodes):
        c=a-(i+1)
        b+= factorial(a)/(factorial(i+1)*factorial(a-(i+1)))
    possibleRequestGraphs = [Graph(numberOfNodes) for j in range(int(b))]
    #for j in range(int(b)):
    #    print(possibleRequestGraphs[j])
    print(possibleEdgePermutations)
    for i in range(numberOfNodes):
        for j in range(lengths[i]):
            for k in range(int(b)):
                print(possibleRequestGraphs[k])
            #print("outside loop: \n",possibleRequestGraphs[j])
            for k in range(i+1):
                print("possible permutations ",i," ",j, " ", k," ", 0, " : ",possibleEdgePermutations[i][j][k][0])
                print("possible permutations ",i," ",j, " ", k," ", 1, " : ",possibleEdgePermutations[i][j][k][1])
                print("request graph before: \n ", possibleRequestGraphs[j])
                print("j,k values: ",j,",",k)
                possibleRequestGraphs[j].addEdge(possibleEdgePermutations[i][j][k][0],possibleEdgePermutations[i][j][k][1])  
                print("request graph After: \n ", possibleRequestGraphs[j])
            
            print("possibleRequestGraph: ",j, "\n",possibleRequestGraphs[i])
    
    return possibleRequestGraphs
        
def longestTrailAlgorithm(graph, timeLimit):
    pathsTaken = 0
    profit = 0
    t=0
    while (t< timeLimit):
        longestPath = graph.findLongestPath()
        print(graph)
        print("longest path",longestPath)
        for i in range(len(longestPath)-1):
            graph.deleteEdge(longestPath[i],longestPath[i+1])
            print(graph)

        pathsTaken+=1
        t+=len(longestPath)

    profit = timeLimit-pathsTaken+1
    return profit

        
def opt(graph, timeLimit):
    '''
    for each vertex

    '''


            
            



def main():
    possibleRequestGraphs = generateRequestGraphs(3, 3)
    for graph in possibleRequestGraphs:
        print(graph)
    #print(list(possibleRequestGraphs))
    for graph in possibleRequestGraphs:
        if graph.isCyclic():
           pass
        else:
            print(longestTrailAlgorithm(graph,3))
    
   #graph = Graph(len(list(g.keys())),g)
   # print(longestTrailAlgorithm(graph,3))

main()

    