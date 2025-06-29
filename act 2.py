import numpy as np
import matplotlib.pyplot as plt

# Tiempo discreto
n = np.arange(-10, 11)

# Señales elementales
delta = np.where(n == 0, 1, 0)               # Pulso unitario
u = np.where(n >= 0, 1, 0)                   # Escalón unitario
rampa = np.where(n >= 0, n, 0)               # Rampa
seno = np.sin(0.2 * np.pi * n)              # Señal seno
coseno = np.cos(0.2 * np.pi * n)            # Señal coseno
expo = np.exp(0.1 * n)                       # Exponencial creciente

# Graficar todas
fig, axs = plt.subplots(3, 2, figsize=(10, 8))

axs[0, 0].stem(n, delta,)
axs[0, 0].set_title("Pulso unitario δ[n]")

axs[0, 1].stem(n, u,)
axs[0, 1].set_title("Escalón unitario u[n]")

axs[1, 0].stem(n, rampa,)
axs[1, 0].set_title("Rampa r[n]")

axs[1, 1].stem(n, seno,)
axs[1, 1].set_title("Seno discreto")

axs[2, 0].stem(n, coseno,)
axs[2, 0].set_title("Coseno discreto")

axs[2, 1].stem(n, expo,)
axs[2, 1].set_title("Exponencial discreta")

plt.tight_layout()
plt.show()
