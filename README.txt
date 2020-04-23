Dial-A-Ride Experimentation Author: Patrick Davis 19'

# DARP- Problem Statement
In the Revenue Dial-a-Ride Problem (RDARP), a driver, often referred to as a server, moves around in a metric space serving ride requests to gain revenue.
Each request includes a source, destination and revenue.
The input set of requests can be represented by a directed graph with locations as vertices and requests as edges. We will refer to this graph as the request graph.
Objective: Given the request graph, the metric space, and time limit, T, maximize the total revenue
We study a basic variation of RDARP to understand the underlying challenges of the problem. Our variation makes two main assumptions on the request graph:
It lies in a uniform metric space, i.e., each vertex is equal distance away from any other vertex
The revenues are uniform. The uniform revenue allows us to equivalently state the optimization objective of this problem as serving the maximum number of requests in the given time, T.
# Simulation
We consider a greedy algorithm, Longest Trail First (LTF), which repeatedly serves the longest trail of remaining requests available in the request graph until reaching time limit T.
A trail is a connected set of edges which a server can follow without repeating an edge.
Finding the longest trail in a general graph is an NP-hard problem, thus making LTF not able to run in polynomial time.
For a directed and acyclic graph (DAG), it is well known that one can find the longest path in polynomial time. Note that the longest trail and longest path in a DAG are the same.
The algorithm uses the known poly-time routine of finding the longest path in a DAG to create a  sequence of requests which the server can satisfy in the given time limit.


Files:
DarpExperimentation.py -  This is the main file in which the algorithms are defined, and the main function runs them
                           and displays results in a graph

Graph.py -                This contains the graph class, which has methods to find the longest path, topologically sort,
                            and to check if there is a cycle

GraphGenerator.py -        This contains methods to create graphs to be tested on

requirements.txt -        This contains a list of all the packages that you will need. If you don't know how to set up
                            a virtual enviornment (to keep packages separated and organized), then I suggest watching:
                            https://www.youtube.com/watch?v=_5GVj5bqf9w
                            It is much easier than it sounds at first, and it makes it quick and easy to install
                            anything you need.

