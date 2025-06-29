import numpy as np
import matplotlib.pyplot as plt

# Tiempo continuo simulado
t = np.linspace(-2, 2, 1000)
dt = t[1] - t[0]
N = len(t)
f = np.fft.fftshift(np.fft.fftfreq(N, d=dt))

x1 = np.sin(2 * np.pi * 1 * t)
x2 = np.cos(2 * np.pi * 3 * t)
x = 2 * x1 + 0.5 * x2

X1 = np.fft.fft(x1)
X2 = np.fft.fft(x2)
X = np.fft.fft(x)

# Verificamos: X ≈ 2*X1 + 0.5*X2
error = np.max(np.abs(X - (2 * X1 + 0.5 * X2)))
print("Error de linealidad:", error)
