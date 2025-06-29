import numpy as np
import matplotlib.pyplot as plt

# Tiempo
t = np.linspace(-5, 5, 1000)
dt = t[1] - t[0]  # intervalo de muestreo

# Señal 1: Pulso rectangular
pulso_rect = np.where((t >= -1) & (t <= 1), 1, 0)

# Señal 2: Señal senoidal
f = 2  # Hz
seno = np.sin(2 * np.pi * f * t)

# Escalón unitario
escalon = np.where(t >= 0, 1, 0)

# FFT de cada señal
def plot_fft(signal, t, title):
    N = len(signal)
    fft_vals = np.fft.fft(signal)
    fft_freq = np.fft.fftfreq(N, d=dt)
    fft_vals_shifted = np.fft.fftshift(fft_vals)
    fft_freq_shifted = np.fft.fftshift(fft_freq)
    magnitude = np.abs(fft_vals_shifted) / N

    plt.figure(figsize=(10, 4))
    plt.plot(fft_freq_shifted, magnitude)
    plt.title(f"Transformada de Fourier de {title}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Graficar FT
plot_fft(pulso_rect, t, "Pulso rectangular")
plot_fft(seno, t, "Señal senoidal")
plot_fft(escalon, t, "Señal escalon unitario")
