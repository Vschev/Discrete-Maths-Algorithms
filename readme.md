
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

1 2 3 4 2

Global.py - a DNA aligner, uses the Needleman-Wunsch algorithm for the global alignment. Takes two DNA sequences (caps only) as two strings and returns an alignment.
Scores for gaps/mismatches/matches can be modified within the script.

Global_affinity.py - this one uses an "affine gap" model, in which the penalty for a gap opening is different from lengthening it.
It also requires two sequences and the third string of two numbers: penalties for an opening and the continuation.

Global_blosum.py - a protein aligner using the BLOSUM62 score matrix for amino acids (presented as a dictionary of scores within the script, modifiable).
Takes two protein sequences as its input and returns the best global alignment

Promoter prediction.py

This script utilizes the Viterbi algorithm to predict promoter regions in the given DNA sequence.
A sequence of DNA nucleotides is taken as an input (a string consisting of 'A', 'C', 'G', 'T' characters, caps only).
The sequence of P/N characters is returned as an output, for promoter and non-promoter loci, respectively.
Model parameters are modifiable within the script (probability to emit A/C/G/T from P and non-P states; chances to stay at P, stay at NP or change from one to another).

RNA predictor.py

This file predicts the optimal secondary structure of an RNA molecule based on dynamic programming.
It tries to maximise an amount of complementary interactions that the molecule has with itself.
Taking RNA sequence as an input (caps only), it returns the sequence of characters showing GC and AT interactions as parentheses and unpaired bases as dots.
(Refer also to the RNA.png)

Sample Input:
GCUGAUGGCAU

Sample Output:
.(.)(((.)))
