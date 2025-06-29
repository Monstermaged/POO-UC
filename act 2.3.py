import numpy as np
import matplotlib.pyplot as plt

# Tiempo continuo simulado
t = np.linspace(-5, 5, 1000)
dt = t[1] - t[0]

# Señal 1: Pulso rectangular
pulso = np.where((t >= -1) & (t <= 1), 1, 0)

# Señal 2: Señal senoidal
f = 2  # frecuencia en Hz
seno = np.sin(2 * np.pi * f * t)

# Función para graficar espectro (magnitud y fase)
def graficar_fft(signal, t, nombre):
    N = len(signal)
    fft_vals = np.fft.fft(signal)
    fft_freqs = np.fft.fftfreq(N, d=dt)
    
    # Centrar el espectro en 0 Hz
    fft_vals_shifted = np.fft.fftshift(fft_vals)
    fft_freqs_shifted = np.fft.fftshift(fft_freqs)

    magnitud = np.abs(fft_vals_shifted) / N
    fase = np.angle(fft_vals_shifted)

    # Graficar
    plt.figure(figsize=(12, 5))

    # Magnitud
    plt.subplot(1, 2, 1)
    plt.plot(fft_freqs_shifted, magnitud)
    plt.title(f"Espectro de Magnitud: {nombre}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid(True)

    # Fase
    plt.subplot(1, 2, 2)
    plt.plot(fft_freqs_shifted, fase)
    plt.title(f"Espectro de Fase: {nombre}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Fase (rad)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Aplicar a ambas señales
graficar_fft(pulso, t, "Pulso Rectangular")
graficar_fft(seno, t, "Señal Senoidal")
