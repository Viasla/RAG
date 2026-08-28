# Intuition
An a‑unshuffle can be thought of as the reverse operation of an a‑shuffle: it records how a deck was cut into a piles and then interleaved, and by ‘undoing’ that interleaving one recovers the original ordered deck.

The coding scheme labels each card according to which of the a piles it originated from; the positions of these labels in a tuple M describe exactly how the cards were interleaved, so the a‑unshuffle simply reads off that labeling to reconstruct the pre‑shuffle order.

