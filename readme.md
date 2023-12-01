Eulerian way.py - this file contains an implementation of an algorithm finding the Eulerian path in a graph, if it exists.
Eulerian path goes through all of the edges in the graph, and only once.
An input for this file is a list of strings representing a graph.
The first string contains two numbers (whitespace separated): numbers of the vertices and edges in the graph.
Each of the consequent strings desribe an edge in the graph and contains two numbers - vertices where it begins and ends.
An output is a string of numbers showing a possible eulerian path (first one found by the algorithm).

Sample input:

4 5
1 2
2 1
2 3
3 4
4 2

Sample output:

1 2 3 4 2
