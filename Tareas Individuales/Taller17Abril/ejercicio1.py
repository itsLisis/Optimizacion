import pulp

# Datos
ganancias    = [180, 220]        # Ganancia por tonelada (F1, F2)
disponible_A = 120               # kg disponibles de compuesto A
disponible_B = 80                # kg disponibles de compuesto B
disponible_C = 150               # kg disponibles de compuesto C

# Configuracion del problema
prob = pulp.LpProblem('Fertilizantes', pulp.LpMaximize)

# Variables de decision: toneladas producidas de F1 y F2
x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)

# Funcion objetivo: maximizar ganancia total
prob += ganancias[0]*x1 + ganancias[1]*x2

# Restricciones de compuestos disponibles
prob += 3*x1 + 4*x2 <= disponible_A   # Compuesto A
prob += 2*x1 + 1*x2 <= disponible_B   # Compuesto B
prob += 5*x1 + 3*x2 <= disponible_C   # Compuesto C

# Resolucion
prob.solve(pulp.PULP_CBC_CMD(msg=0))

print("="*30)
print("Ejercicio 1: Mezcla de fertilizantes")
print(f"F1 producido (x1): {x1.value():.4f} toneladas")
print(f"F2 producido (x2): {x2.value():.4f} toneladas")
print(f"Ganancia maxima Z: ${pulp.value(prob.objective):.2f}")