from fsm import FSM

def compute_binary_mod(N):
    """
    Construct a binary mod-N finite state machine (FSM) that accepts binary strings divisible by N.

    Args:
        N: The modulus (positive integer).
        input_seq: The binary input sequence (string of '0' and '1').

    Returns:
        An FSM instance representing the mod-N automaton for binary inputs.
    """
    
    states = {f"S{i}" for i in range(N)} # The define number of States; for the mod 3 problem - the number of states corresponds to the divisor; each state determines a possible remainder when divided by divisor
    transitions = {} # define transitions as a dictionary ; The criterion that maps one state to another
    for r in range(N):
        for b in {'0','1'}:
            new_r = (r * 2 + int(b)) % N # transition criteria ; for the number to be divisible by N; 
            transitions[(f"S{r}", b)] = f"S{new_r}" # transition [key] = value; where key = current_state, input symbol; value = next_state
    return FSM(
        states=states,
        transitions=transitions,
        start_state="S0",
        final_states={"S0"} # for the number to be divisible by N; the final state needs to be S0 -> remainder 0
    )