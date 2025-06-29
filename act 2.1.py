import numpy as np
import matplotlib.pyplot as plt

# Tiempo continuo
t = np.linspace(-5, 5, 1000)

# Pulso rectangular entre -1 y 1
pulso_rect = np.where((t >= -1) & (t <= 1), 1, 0)

# Escalón unitario
escalon = np.where(t >= 0, 1, 0)

# Señal senoidal
f = 1      # frecuencia en Hz
senoidal = np.sin(2 * np.pi * f * t)

# Graficar
plt.figure(figsize=(12, 8))

# Pulso rectangular
plt.subplot(3, 1, 1)
plt.plot(t, pulso_rect, label="Pulso rectangular", color='red')
plt.title("Pulso Rectangular")
plt.grid(True)
plt.ylim(-0.2, 1.2)

# Escalón unitario
plt.subplot(3, 1, 2)
plt.plot(t, escalon, label="Escalón unitario", color='blue')
plt.title("Escalón Unitario u(t)")
plt.grid(True)
plt.ylim(-0.2, 1.2)

# Señal senoidal
plt.subplot(3, 1, 3)
plt.plot(t, senoidal, label="Señal senoidal", color='green')
plt.title("Señal Senoidal")
plt.grid(True)

plt.tight_layout()
plt.show()