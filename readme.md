This file predicts the optimal secondary structure of an RNA molecule based on dynamic programming.
It tries to maximise an amount of complementary interactions that the molecule has with itself.
Taking RNA sequence as an input (caps only), it returns the sequence of characters showing GC and AT interactions as parentheses and unpaired bases as dots.
(Refer also to the picture)

Sample Input:
GCUGAUGGCAU

Sample Output:
.(.)(((.)))
