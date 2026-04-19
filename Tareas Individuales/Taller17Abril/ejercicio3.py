import numpy as np
from scipy.integrate import odeint

# Datos
beta  = 0.00003    # Tasa de contagio por dia
gamma = 0.1        # Tasa de recuperacion por dia
N     = 10000      # Poblacion total
I0    = 50         # Infectados iniciales
dias  = 200        # Dias a simular

# Funcion: tasa de cambio de infectados
# dI/dt = beta*(N - I)*I - gamma*I
def modelo_SIS(I, t):
    return beta * (N - I) * I - gamma * I

# Configuracion
t = np.linspace(0, dias, 1000)

# Resolucion
I = odeint(modelo_SIS, I0, t)

print("="*30)
print("Ejercicio 3: Epidemia en una ciudad")
print(f"Equilibrio endemico teorico: {N - gamma/beta:.2f} infectados")
print(f"Valor simulado al dia {dias}: {I[-1][0]:.2f} infectados")