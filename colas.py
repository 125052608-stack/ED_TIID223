from collections import deque 

""" crear lista de personas """
cola  = deque(["Ana","Carlos"])

cola.append("Jorge")
cola.append("Andres")
print("Cola actual: ",cola)

atendido = cola.popleft()
print(f"se atendió a: {atendido}")

print("Cola restante: ",cola)

atendido = cola.popleft()
print(f"se atendió a: {atendido}")

print("Cola restante: ",cola) 