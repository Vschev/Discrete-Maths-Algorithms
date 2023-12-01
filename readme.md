Promoter prediction.py
This script utilizes the Viterbi algorithm to predict promoter regions in the given DNA sequence.

Promoter prediction.py - a sequence of DNA nucleotides is taken as an input (a string consisting of 'A', 'C', 'G', 'T' characters, caps only).
The sequence of P/N characters is returned as an output, for promoter and non-promoter loci, respectively.
Model parameters are modifiable within the script (probability to emit A/C/G/T from P and non-P states; chances to stay at P, stay at NP or change from one to another).
