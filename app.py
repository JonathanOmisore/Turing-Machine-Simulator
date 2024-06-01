from flask import Flask, request, render_template
from TuringMachine import TuringMachine
app = Flask(__name__)
turing_machine = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/initialize', methods=['POST'])
def initialize():
    global turing_machine
    tape = request.form['tape']
    initial_state = request.form['initial_state']
    final_states = request.form['final_states'].split(',')
    transition_function = {
        (line.split(',')[0], line.split(',')[1]): (line.split(',')[2], line.split(',')[3], line.split(',')[4])
        for line in request.form['transition_function'].split('\n') if line.strip()
    }
    print(f"Initialized with tape: {tape}")
    print(f"Initial state: {initial_state}")
    print(f"Final states: {final_states}")
    print(f"Transition function: {transition_function}")
    turing_machine = TuringMachine(tape, initial_state, final_states, transition_function)
    return render_template('machine.html', tape=turing_machine.get_tape(), state=turing_machine.get_state(), head=turing_machine.get_head_position(), finished=False)

@app.route('/step', methods=['POST'])
def step():
    global turing_machine
    if turing_machine:
        finished = turing_machine.step()
        return render_template('machine.html', tape=turing_machine.get_tape(), state=turing_machine.get_state(), head=turing_machine.get_head_position(), finished=finished)
    return "Turing Machine not initialized", 400

if __name__ == '__main__':
    app.run(debug=True)
