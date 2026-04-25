from qiskit import QuantumCircuit

# Create a simple quantum circuit
qc = QuantumCircuit(1)

# Apply Hadamard gate (superposition)
qc.h(0)

print(qc)
