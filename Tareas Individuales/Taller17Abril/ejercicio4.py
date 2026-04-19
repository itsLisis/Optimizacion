# Datos
P0    = 400     # Poblacion inicial de peces
r     = 0.4     # Tasa de crecimiento intrinseca
K     = 1000    # Capacidad maxima de la laguna
H     = 80      # Peces extraidos por año
años = 10      # Años a simular

# Resolucion: aplicar recurrencia año a año
# P_{n+1} = P_n + r*P_n*(1 - P_n/K) - H
P = P0

print("="*30)
print("Ejercicio 4: Modelo logistico de pesca")
print(f"Año 0: P={P:.2f} peces")

for n in range(1, años + 1):
    P = P + r*P*(1 - P/K) - H
    print(f"Año {n}: P={P:.2f} peces")
    if P <= 0:
        print("Se extingue la poblacion")
        break