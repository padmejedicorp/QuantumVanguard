#pivotaltracker
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# Create a quantum circuit with 3 qubits and 3 classical bits
circuit = QuantumCircuit(3, 3)

# Create a random initial state for the qubit to be teleported
initial_state = [0.3, 0.6]  # Example state vector
circuit.initialize(initial_state, 0)

# Create entangled Bell pair (qubits 1 and 2)
circuit.h(1)
circuit.cx(1, 2)
#Token: 53974b42220b59eab5185630da896b74 

# Apply a CNOT gate and Hadamard gate to the qubit to be teleported (qubit 0)
circuit.cx(0, 1)
circuit.h(0)
#Project: 2677298

# Measure the qubits to be teleported (qubits 0 and 1)
circuit.measure([0, 1], [0, 1])

# Apply conditional gates based on measurement outcomes
circuit.cx(1, 2)
circuit.cz(0, 2)


# Measure the result and store it in a classical bit (qubit 2)
circuit.measure(2, 2)

# Simulate the quantum circuit using a local simulator
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(circuit, simulator)
job = execute(compiled_circuit, simulator, shots=1024)
result = job.result()


# Display the measurement results
counts = result.get_counts()
print("Measurement results:")
print(counts)

# Visualize the quantum state on the Bloch sphere for the teleported qubit (qubit 2)
backend_statevector = Aer.get_backend('statevector_simulator')
statevector = execute(circuit, backend_statevector).result().get_statevector()
plot_bloch_multivector(statevector)

# Visualize the measurement results as a histogram
plot_histogram(counts)
