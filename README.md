# Finite State Machine (FSM) - Modulo-N Binary Checker

This project implements a **generic Finite State Machine (FSM)** in Python to determine whether a binary string represents a number divisible by a given integer `N`.

It supports:
- Any Mod-N FSM (e.g., mod 3, mod 5)
- Custom FSM configuration using states, transitions, and final states
- A clean OOP design that is easy to extend and test

---

## Problem Statement

> Build a reusable FSM that, given a binary string, determines whether it is divisible by `N` using only finite state transitions.

---

## Features

- Generic FSM class: accepts any finite set of states, transitions, start state, and final states
- Supports any mod-N configuration (mod 2, 3, 5, etc.)
- Final state check determines acceptance
- Fully testable with Python's `unittest`

---

## FSM Background

A finite state machine is defined by a 5-tuple:

**FSM = (Q, Σ, δ, q₀, F)**

Where:
- `Q`: Set of states
- `Σ`: Input alphabet (e.g., `{0, 1}`)
- `δ`: Transition function
- `q₀`: Start state
- `F`: Accepting (final) states

For a Mod-3 FSM:
- States: `S0`, `S1`, `S2` represent remainders 0, 1, 2
- Final state: `S0` (only if the binary number is divisible by 3)

---

## Usage

### Run a divisibility check:

```python
from mod_fsm import compute_mod

input_sequence = "110"  # binary 6
fsm = compute_mod(3, input_sequence)

print(fsm.is_accepted(input_sequence))  
```

## Project Structure 

```

fsm_mod_project/
├── fsm.py              # Generic FSM class
├── mod_fsm.py          # Mod-N FSM generator
├── main.py             # Example usage or CLI
├── tests/
│   └── test_fsm.py     # Unit tests
└── README.md   

```
