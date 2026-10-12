n = int(input("Total de datos (n): "))
k = int(input("Número de intervalos (k): "))
E = n / k

print(f"\nIngresa las {k} frecuencias observadas (Oi):")
O = [float(input(f"  Intervalo {i+1}: ")) for i in range(k)]

chi2 = 0
print("\nIntervalo\t\tOi\tEi\tChi²")
print("-" * 35)

etiquetas = []
for i in range(k):
    oi = O[i]
    term = ((oi - E) ** 2) / E
    chi2 += term
    
    inf = i / k
    sup = (i + 1) / k
    etiqueta = f"{inf:.1f}-{sup:.1f}"
    etiquetas.append(etiqueta)
    
    print(f"{etiqueta}\t\t{oi:.0f}\t{E:.2f}\t{term:.2f}")

gl = k - 1
critico = 16.919  

print(f"\nChi² Calculada: {chi2:.4f}")
print(f"Chi² Crítica:   {critico}")

if chi2 < critico:
    print("Resultado: NO SE RECHAZA H0 (Uniforme aceptable)")
else:
    print("Resultado: SE RECHAZA H0 (No uniforme)")

plt.figure(figsize=(9, 5))
plt.bar(etiquetas, O, width=0.4, label='Frecuencia Observada (Oi)', color='skyblue', edgecolor='black')
plt.axhline(y=E, color='red', linestyle='--', linewidth=2, label=f'Frecuencia Esperada (Ei = {E:.2f})')

plt.xlabel('Intervalos', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.title('Prueba de Chi Cuadrada - Uniformidad', fontsize=14, fontweight='bold')
plt.xticks(rotation=30)
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.7)
plt.tight_layout()

plt.show()