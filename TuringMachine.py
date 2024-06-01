class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transition_function):
        self.tape = list(tape)
        self.head = 0
        self.state = initial_state
        self.final_states = set(final_states)
        self.transition_function = transition_function

    def step(self):
        if self.state in self.final_states:
            print(f"Machine has reached final state {self.state}")
            return True  # Machine has reached a final state

        # Ensure the head is within the tape bounds
        if self.head < 0 or self.head >= len(self.tape):
            self.tape.append(' ')
        
        symbol = self.tape[self.head]
        action = self.transition_function.get((self.state, symbol))

        print(f"Current state: {self.state}, Head position: {self.head}, Read symbol: '{symbol}'")
        print(f"Transition function lookup: {self.state}, {symbol}")
        print(f"Action found: {action}")

        if action:
            new_state, new_symbol, direction = action
            print(f"Action: (new_state={new_state}, new_symbol={new_symbol}, direction={direction})")
            self.tape[self.head] = new_symbol
            self.state = new_state
            direction = direction.strip()
            if direction== 'R':
                self.head += 1
            elif direction == 'L':
                self.head -= 1
            else:
                print(f"Unknown direction: {direction}")

            if self.head < 0:
                self.tape.insert(0, ' ')
                self.head = 0
            elif self.head >= len(self.tape):
                self.tape.append(' ')

            print(f"Updated state: {self.state}, Head position: {self.head}, Tape: {''.join(self.tape)}")
        else:
            print("No valid action found, halting.")

        return self.state in self.final_states

    def get_tape(self):
        return ''.join(self.tape).strip()

    def get_state(self):
        return self.state

    def get_head_position(self):
        return self.head
