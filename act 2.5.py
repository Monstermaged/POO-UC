import numpy as np
import matplotlib.pyplot as plt

# Tiempo continuo simulado
t = np.linspace(-2, 2, 1000)
dt = t[1] - t[0]
N = len(t)
f = np.fft.fftshift(np.fft.fftfreq(N, d=dt))

# Función para graficar magnitud y fase
def plot_fft(signal, titulo):
    fft_vals = np.fft.fft(signal)
    fft_vals = np.fft.fftshift(fft_vals)
    magnitude = np.abs(fft_vals) / N
    phase = np.angle(fft_vals)

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(f, magnitude)
    plt.title(f"{titulo} - Magnitud")
    plt.xlabel("Frecuencia (Hz)")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(f, phase)
    plt.title(f"{titulo} - Fase")
    plt.xlabel("Frecuencia (Hz)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# ------------------------------------
# 1.Linealidad
# ------------------------------------
x1 = np.sin(2 * np.pi * 3 * t)
x2 = np.cos(2 * np.pi * 5 * t)
x_sum = 2 * x1 + 0.5 * x2

X1 = np.fft.fft(2 * x1)
X2 = np.fft.fft(0.5 * x2)
X_sum_manual = X1 + X2
X_sum_fft = np.fft.fft(x_sum)

error_linealidad = np.max(np.abs(X_sum_manual - X_sum_fft))
print("Error por linealidad:", error_linealidad)

plot_fft(x_sum, "Suma Lineal (2x1 + 0.5x2)")

# ------------------------------------
# 2.Desplazamiento en el tiempo
# ------------------------------------
x = np.sin(2 * np.pi * 4 * t)
t0 = 0.5  # segundos
x_shifted = np.sin(2 * np.pi * 4 * (t - t0))

X = np.fft.fftshift(np.fft.fft(x))
X_shift = np.fft.fftshift(np.fft.fft(x_shifted))
X_theoretical = X * np.exp(-1j * 2 * np.pi * f * t0)

error_shift = np.max(np.abs(X_shift - X_theoretical))
print("Error por desplazamiento temporal:", error_shift)

plot_fft(x_shifted, f"Desplazamiento en el tiempo t₀={t0}")

# ------------------------------------
# 3.Escalamiento en frecuencia
# ------------------------------------
x = np.sin(2 * np.pi * 1 * t)
a = 2  # compresión temporal
x_scaled = np.sin(2 * np.pi * 1 * a * t)

plot_fft(x, "Original")
plot_fft(x_scaled, f"Escalamiento en frecuencia (a={a})")

