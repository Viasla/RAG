# Intuition
The mean recurrence matrix records only return times: its diagonal entry for state s_i equals the expected number of steps required for the chain, starting at s_i, to return to s_i for the first time, while all off‑diagonal entries are zero. Thus D captures how often each state is revisited, without encoding transitions to other states.

