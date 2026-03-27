Eulerian way.py - this file contains an implementation of an algorithm finding the Eulerian path in a graph, if it exists, which is used in several genome assembly algorithms.
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

RNA predictor.py
1 2 3 4 2
This file predicts the optimal secondary structure of an RNA molecule based on dynamic programming.
It tries to maximise an amount of complementary interactions that the molecule has with itself.
Taking RNA sequence as an input (caps only), it returns the sequence of characters showing GC and AT interactions as parentheses and unpaired bases as dots.
(Refer also to the RNA.png)

Sample Input:
GCUGAUGGCAU

Sample Output:
.(.)(((.)))
