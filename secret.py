from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# Create a quantum circuit with 2 qubits and 2 classical bits
circuit = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit
circuit.h(0)

# Apply a CNOT gate (entanglement) between the first and second qubit
circuit.cx(0, 1)

# Measure the qubits and store the results in classical bits
circuit.measure([0, 1], [0, 1])

# Simulate the quantum circuit using a local simulator
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(circuit, simulator)
job = execute(compiled_circuit, simulator, shots=1024)
result = job.result()

# Display the measurement results
counts = result.get_counts()
print("Measurement results:")
print(counts)

# Visualize the quantum state on the Bloch sphere
backend_statevector = Aer.get_backend('statevector_simulator')
statevector = execute(circuit, backend_statevector).result().get_statevector()
plot_bloch_multivector(statevector)

# Visualize the measurement results as a histogram
plot_histogram(counts)
