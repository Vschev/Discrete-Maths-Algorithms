This branch contains several sequence aligners.

Global.py - a DNA aligner, uses the Needleman-Wunsch algorithm for the global alignment. Takes two DNA sequences (caps only) as two strings and returns an alignment.
Scores for gaps/mismatches/matches can be modified within the script.

Global_affinity.py - this one uses an "affine gap" model, in which the penalty for a gap opening is different from lengthening it.
It also requires two sequences and the third string of two numbers: penalties for an opening and the continuation.

Global_blosum.py - a protein aligner using the BLOSUM62 score matrix for amino acids (presented as a dictionary of scores within the script, modifiable).
Takes two protein sequences as its input and returns the best global alignment
