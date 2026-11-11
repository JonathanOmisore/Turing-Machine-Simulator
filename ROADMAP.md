# Development Roadmap

## Vision

Grow **Turing Machine Simulator** from a focused Turing machine application into an interactive environment for exploring **models of computation**. The long-term goal is to let users define machines, step through executions, inspect state changes, and compare computational models through a consistent interface.

This document describes **planned work**, not features already implemented. Priorities, designs, and estimates may change as development progresses.

## Goals

- Preserve and improve the existing Turing machine simulator.
- Separate computation logic from the web interface so additional models are easier to implement.
- Make executions inspectable through step-by-step controls, traces, interactive state diagrams, and animations.
- Build a coherent, responsive, accessible interface whose visual components can be reused across computation models.
- Support importing, exporting, testing, and sharing example machine definitions without requiring personal or sensitive data.
- Provide understandable documentation and examples for students, enthusiasts, and developers exploring theoretical computer science.

## Milestones

### Milestone 1: Strengthen the existing Turing machine simulator

**Estimated effort: 8–12 hours**  
**Priority: High**  
**Status: Planned**

- [ ] Audit and document existing capabilities, expected inputs, and edge cases.
- [ ] Refactor simulation logic into a clearly defined engine separate from UI concerns.
- [ ] Define consistent representations for states, alphabets, transitions, tapes, and machine configurations.
- [ ] Improve validation and error messages for invalid machine definitions.
- [ ] Add tests for halting, accepting/rejecting, tape movement, and boundary conditions.
- [ ] Document local setup, test execution, and a sample machine.

**Done when:** Existing functionality is preserved, core logic has automated tests, and a new contributor can run a working example using the documentation.

### Milestone 2: Unified execution and visualization interface

**Estimated effort: 8–12 hours**  
**Priority: High**  
**Status: Planned**

- [ ] Define a common execution interface with `initialize`, `step`, `run`, and `reset` operations (or an equivalent design).
- [ ] Add or improve execution controls for stepping, pausing, resetting, and setting a maximum step count.
- [ ] Show the current state, active transition, tape contents, and read/write head position.
- [ ] Provide a readable execution trace for debugging.
- [ ] Handle long-running or non-halting executions safely with configurable limits.
- [ ] Improve accessibility and mobile layout where practical.

**Done when:** Users can follow an execution step by step and understand why each state transition happened.

### Milestone 3: Interactive visual design and user experience

**Estimated effort: 25–40 hours (some tasks overlap with Milestone 2)**  
**Priority: High**  
**Status: Planned**

- [ ] **Visual foundation (5–8 hours):** Establish consistent layouts, typography, spacing, color tokens, light/dark contrast, and navigation for the simulator.
- [ ] **Responsive UI (4–6 hours):** Redesign machine configuration panels, execution views, and controls for desktop, tablet, and mobile screens.
- [ ] **State-transition diagrams (7–11 hours):** Build interactive graphs of machine states and labeled transitions, clearly identifying the start, current, accept, and reject states where applicable.
- [ ] **Execution animation (4–6 hours):** Highlight the active state and transition, and animate changes to tape cells and head position without obscuring the underlying machine state.
- [ ] **Reusable visual components (3–5 hours):** Extract diagram, execution controls, status indicators, and step-history UI so they can be adapted for DFA, NFA, PDA, and other models.
- [ ] **Accessibility and usability (2–4 hours):** Add keyboard-accessible controls, meaningful labels, reduced-motion support, strong contrast, and clear error/empty states.
- [ ] Validate the design with realistic sample machines and document any tradeoffs or deferred work.

**Done when:** The existing Turing machine can be inspected in a visually clear, responsive interface; execution states and transitions are understandable without reading raw logs; keyboard and reduced-motion users have usable alternatives; and key UI elements are designed for reuse.

> These estimates describe planned work, not implemented features. The shared step controls and basic state display in Milestone 2 overlap with this milestone, so totals should not double-count that work.

### Milestone 4: Deterministic finite automata (DFA)

**Estimated effort: 8–12 hours**  
**Priority: High**  
**Status: Planned**

- [ ] Implement DFA definitions, transition validation, and execution.
- [ ] Display active states, transitions, and whether an input string is accepted.
- [ ] Provide examples for common regular languages.
- [ ] Add unit and integration tests for acceptance and rejection.
- [ ] Document how DFAs differ from Turing machines.

**Done when:** Users can define a DFA, run a string through it, and inspect the result and execution history.

### Milestone 5: Nondeterministic finite automata (NFA)

**Estimated effort: 8–14 hours**  
**Priority: Medium**  
**Status: Planned**

- [ ] Support multiple transitions from a state and epsilon transitions.
- [ ] Implement epsilon closure and active-state-set execution.
- [ ] Visualize multiple simultaneous possible states without implying a single deterministic path.
- [ ] Test ambiguous transitions, epsilon cycles, and empty-string acceptance.
- [ ] Add examples comparing equivalent DFAs and NFAs.

**Done when:** Users can run NFAs and inspect the set of reachable states after each input symbol.

### Milestone 6: Pushdown automata (PDA)

**Estimated effort: 12–18 hours**  
**Priority: Medium**  
**Status: Planned**

- [ ] Design a machine definition with stack alphabet and push/pop operations.
- [ ] Implement a PDA execution engine with bounded exploration for nondeterministic branches.
- [ ] Visualize stack changes alongside state transitions.
- [ ] Provide examples such as balanced parentheses.
- [ ] Add tests for stack underflow, acceptance modes, and branch limits.

**Done when:** Users can explore stack-based computation interactively and inspect stack operations during execution.

### Milestone 7: Advanced models

**Estimated effort: 18–30 hours total (subject to scope)**  
**Priority: Later**  
**Status: Exploratory**

- [ ] **Multi-tape Turing machines:** Model multiple tapes and heads; display synchronized tape changes.
- [ ] **Register machines:** Implement registers, instructions, and a step-by-step execution trace.
- [ ] **Lambda calculus:** Parse expressions, perform capture-avoiding substitution, and visualize beta-reduction steps.

These may be split into separate milestones after the core architecture is stable. Each model will have its own design review, test cases, and examples.

### Milestone 8: Project polish and release readiness

**Estimated effort: 6–10 hours**  
**Priority: Ongoing**  
**Status: Planned**

- [ ] Add a catalog of runnable examples for supported models.
- [ ] Evaluate a versioned, documented format for saving and loading machine definitions.
- [ ] Expand the README with screenshots or a short demonstration.
- [ ] Set up continuous integration to run tests on pull requests.
- [ ] Improve error handling and user-facing documentation.
- [ ] Prepare a tagged release and changelog once a coherent milestone is completed.

**Done when:** The project is easy to install, test, understand, and use without developer assistance.

## Suggested sequence

1. Stabilize the existing Turing machine engine and tests.
2. Establish a shared execution interface, then redesign the visual layout and controls.
3. Build interactive state diagrams, execution animations, and reusable visualization components.
4. Implement DFA support, then NFA support, extending the reusable visuals as needed.
5. Add pushdown automata, including a dedicated stack visualization.
6. Evaluate and prioritize advanced models based on complexity and user interest.
7. Prepare a release with examples and documentation.

## Effort and scope

The first **two milestones represent approximately 16–24 hours** of planned development. The new visual design milestone adds approximately **25–40 hours of scoped tasks**, some of which overlap with Milestone 2. Across all eight milestones, the gross task estimates total **93–148 hours before accounting for overlap**. These figures are rough planning estimates, **not completed hours, promised delivery dates, or guaranteed paid hours**.

## Project boundaries

- Focus on mathematical and theoretical **models of computation** and educational software tooling.
- Do not include training, fine-tuning, evaluating, or benchmarking machine-learning or frontier AI models.
- Use synthetic/sample inputs in examples and tests; do not commit secrets or real personal data.
- Maintain authentic Git history and track actual progress through issues and commits.

## Progress tracking

As work starts, convert selected checklist items into GitHub Issues, link related pull requests, and change their status only when completed. Review estimates and priorities after each milestone.

---

**Roadmap status:** Draft for upcoming independent development.  
**Repository:** [JonathanOmisore/Turing-Machine-Simulator](https://github.com/JonathanOmisore/Turing-Machine-Simulator)
