class FSM:
    def __init__(self,
        states: set[str],
        transitions: dict[tuple[str, any], str],
        start_state: str,
        final_states: set[str] = None,
        outputs: dict[str, any] = None,
    ):
        """
        Initialize the FSM.

        Args:
            states: Set of states.
            transitions: Dict mapping (state, input_symbol) -> next_state.
            start_state: The initial state.
            final_states: Set of accepting states.
            outputs: Optional dict mapping state -> output value.
        Raises:
            Value Errors if start_states and final_states not present in the states and final_states sets respectively
        """
        if start_state not in states:
            raise ValueError(f"start_state {start_state} not in states")
        if final_states:
            if not final_states.issubset(states):
                raise ValueError("final_states must be subset of states")
        self.states = states
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states if final_states else set()
        self.outputs = outputs if outputs else {}
        self.current_state = start_state

    def reset(self):
        """Reset FSM to the start state."""
        self.current_state = self.start_state

    def process(self, input_symbol):
        """
        Process a single input symbol, update state, and return output if any.

        Args:
            input_symbol: The input symbol to process.

        Returns:
            The output value associated with the new current state or None.
        
        Raises:
            ValueError: If no transition exists for (current_state, input_symbol).
        """
        key = (self.current_state, input_symbol) # set the key as the current_state and the input symbol
        if key not in self.transitions:
            raise ValueError(f"No transition for ({self.current_state}, {input_symbol})")
        self.current_state = self.transitions[key] # set the current state -> next state
        return self.outputs.get(self.current_state) # gets the value associated with the current state else returns none.

    def process_sequence(self, input_sequence):
        """
        Process a sequence of input symbols and return the list of outputs.

        Args:
            input_sequence: List of input symbols.

        Returns:
            List of output values corresponding to each input processed.
        """
        if not all(symbol in {'0', '1'} for symbol in input_sequence):
            raise ValueError(f"Input must be a binary string. Found: {set(input_sequence)}")
        self.reset()
        output_sequence = []
        for symbol in input_sequence:
            output = self.process(symbol)
            output_sequence.append(output)
        return output_sequence # only used if the outputs of the sequence are desired

    def is_accepted(self, input_sequence):
        """
        Check if the FSM accepts the given input sequence.

        Args:
            input_sequence: List of input symbols.

        Returns:
            True if the FSM ends in an accepting state after processing the sequence.
        """
        if not all(symbol in {'0', '1'} for symbol in input_sequence):
            raise ValueError(f"Input must be a binary string. Found: {set(input_sequence)}")
        self.reset()
        for symbol in input_sequence:
            self.process(symbol)
        if  self.current_state in self.final_states:
            return True
        else:
            return False  
        
