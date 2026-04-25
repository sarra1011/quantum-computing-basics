from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)

print("Superposition circuit:")
print(qc)
