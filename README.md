# Turing Machine Simulator

A Python and Flask web application for exploring how Turing machines execute computations, one transition at a time.

This is an independently developed personal project. Its current implementation focuses on a single-tape Turing machine, and its long-term direction is to become an interactive **computational models simulator** supporting multiple models of computation.

## Overview

A Turing machine is an abstract model of computation consisting of a tape, a read/write head, a set of states, and transition rules. This project lets you define a machine in a web form, initialize its tape, and step through its execution to see how the machine changes state and updates the tape.

The simulator is intended for people exploring theoretical computer science, automata, and the mechanics of computation.

## Current features

- Configure an initial tape, initial state, and final states.
- Enter transition rules for the machine.
- Initialize a simulation from a web interface.
- Advance the simulation one step at a time.
- Display the current tape, state, and head position.
- Expand the tape as the head moves beyond its current boundaries.

**Project status:** Early-stage personal project, being resumed for further development. The models listed in the roadmap below are planned, not currently implemented.

## Tech stack

- **Python**: Turing machine simulation logic
- **Flask**: HTTP routes and server-side rendering
- **HTML templates and static assets**: Web interface

## Getting started

### Prerequisites

- Python 3
- `pip`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JonathanOmisore/Turing-Machine-Simulator.git
   cd Turing-Machine-Simulator
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install Flask:

   ```bash
   python -m pip install flask
   ```

4. Start the application:

   ```bash
   python app.py
   ```

5. Visit <http://127.0.0.1:5000> in your browser.

**Note:** The current `app.py` runs Flask with debug mode enabled. Use it only in a trusted local development environment, not as a production deployment.

## Using the simulator

1. Open the web interface.
2. Enter an initial tape, such as `111`.
3. Enter an initial state, such as `q0`.
4. Specify one or more final states, such as `qf`.
5. Enter transition rules, one per line, in this format:

   ```text
   current_state,read_symbol,next_state,write_symbol,direction
   ```

   For example:

   ```text
   q0,1,q0,1,R
   q0, ,qf, ,R
   ```

   This example moves right across the input `1` symbols and transitions to `qf` on a blank space. The blank symbol in the current implementation is a space character. Use uppercase `L` and `R` for movement.

6. Initialize the machine, then use the step control to advance the simulation and inspect its state.

The application currently parses transition lines by commas, so follow the exact five-field format without adding spaces around ordinary fields. Final states are entered as a comma-separated list.

## Repository structure

```text
Turing-Machine-Simulator/
├── TuringMachine.py  # Tape, head, states, and transition logic
├── app.py            # Flask application and simulation routes
├── templates/        # HTML views
└── static/           # Frontend assets
```

## Development roadmap

The next phase will expand the project beyond the classical single-tape Turing machine. Planned work includes:

### Simulation foundations

- [ ] Separate simulator interfaces from individual computation engines.
- [ ] Improve validation of states, symbols, transition rules, and movement directions.
- [ ] Add explicit halt, accept, reject, and error outcomes.
- [ ] Improve tape-boundary behavior and execution controls.
- [ ] Add automated unit and integration tests.

### Additional models of computation

- [ ] **Deterministic finite automata (DFA)**: States, transitions, and string acceptance.
- [ ] **Nondeterministic finite automata (NFA)**: Multiple possible execution paths.
- [ ] **Pushdown automata (PDA)**: Stack-based execution and transition tracing.
- [ ] **Multi-tape Turing machines**: Multiple tape and head configurations.
- [ ] **Register machines**: Instruction-driven computation over registers.
- [ ] **Lambda calculus**: Expression reduction and evaluation strategies.

### Experience and tooling

- [ ] Add interactive state and transition visualizations.
- [ ] Support pausing, resetting, and replaying executions.
- [ ] Allow saving and loading machine definitions.
- [ ] Add worked examples and educational explanations.
- [ ] Improve documentation, accessibility, and UI responsiveness.

These items are proposed development goals rather than promises of implemented functionality. See future issues and development plans for prioritization.

## Known limitations

- Only the existing single-tape Turing machine is implemented; additional computational models are future work.
- Simulation state is stored in a module-level variable in the Flask application, so the current design is not suitable for independent concurrent user sessions.
- Transition parsing and error handling need improvement.
- The code does not yet include a dedicated automated test suite.
- The web application currently uses development-mode settings.

## Contributing

Suggestions, bug reports, and discussions are welcome through [GitHub Issues](https://github.com/JonathanOmisore/Turing-Machine-Simulator/issues).

## Project ownership and license

This project was created independently as a personal software development project, outside university coursework.

**License:** A license has not yet been added to this repository. Before distributing or submitting the project to programs that require an approved open-source license, add an appropriate `LICENSE` file and update this section to match it. Do not assume that a public repository is automatically open-source licensed.
