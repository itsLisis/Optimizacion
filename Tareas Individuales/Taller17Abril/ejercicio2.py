# Datos
S0      = 200    # Sillas iniciales (semana 0)
M0      = 80     # Mesas iniciales (semana 0)
semanas = 10     # Numero de semanas a simular

# Resolucion: aplicar recurrencia semana a semana
S, M = S0, M0

print("="*30)
print("Ejercicio 2: Produccion semanal de una fabrica")
print(f"Semana 0: Sillas={S}, Mesas={M}")

for n in range(1, semanas + 1):
    S_new = 0.6*S + 0.2*M + 40
    M_new = 0.1*S + 0.5*M + 20
    S, M  = S_new, M_new
    print(f"Semana {n}: Sillas={S:.2f}, Mesas={M:.2f}")