# Intuition
A rising sequence is a maximal contiguous block of cards that appear in increasing order when read from left to right; each time the order “drops” a new rising sequence begins.

Thus an ordering can be decomposed uniquely into r such increasing blocks, and r measures how far the ordering is from being completely sorted (which has r=1).

A rising sequence can be thought of as a maximal block of consecutive elements that increase when read from left to right; each time the ordering “drops” a new rising sequence starts.

Equivalently, each “fall” (a position where a larger number is followed by a smaller one) in the inverse permutation creates a new rising sequence in the original ordering.

