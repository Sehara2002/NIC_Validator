# DFA.py

import time

def nic_dfa(nic):
    steps = []   # to store step-by-step transitions
    state = "q0"

    for i, ch in enumerate(nic):
        prev_state = state

        # Digit transitions q0 to q8
        if state.startswith("q") and state[1:].isdigit() and int(state[1:]) <= 8:
            if ch.isdigit():
                state = f"q{int(state[1:]) + 1}"
            else:
                state = "REJECT"

        # q9 decision state
        elif state == "q9":
            if ch in ['V', 'X']:
                state = "ACCEPT"
            elif ch.isdigit():
                state = "q10"
            else:
                state = "REJECT"

        # q10 → q11
        # This part of the code is handling the transition from state "q10" to state "q11" in the DFA
        # (Deterministic Finite Automaton) for validating a National Identity Card (NIC) number.
        elif state == "q10":
            if ch.isdigit():
                state = "q11"
            else:
                state = "REJECT"

        # q11 → accept only if input ends
        elif state == "q11":
            if ch.isdigit():
                state = "ACCEPT"
            else:
                state = "REJECT"

        else:
            state = "REJECT"

        steps.append({
            "step": i + 1,
            "input": ch,
            "from": prev_state,
            "to": state
        })

        if state in ["ACCEPT", "REJECT"]:
            break

    # Length check for incomplete inputs
    if state not in ["ACCEPT", "REJECT"]:
        state = "REJECT"

    return steps, state
