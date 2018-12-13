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

