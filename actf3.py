import numpy as np                  #para trabajar con arrays y funciones metemáticas
import matplotlib.pyplot as plt     #para graficar señales
from scipy.signal import butter, lfilter, freqz #contiene funciones para diseñar y aplicar filtros digitales

# Crear una señal compuesta con varias frecuencias (10,40 y 120Hz)
fs = 1000        # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1.0, fs, endpoint=False) #duración de la señal
x = (np.sin(2*np.pi*10*t) +     # 10 Hz
     np.sin(2*np.pi*40*t) +    # 40 Hz
     np.sin(2*np.pi*120*t))    # 120 Hz

# Función para crear y aplicar filtros
def butter_filter(data, cutoff, fs, order, btype='low'):
    nyq = 0.5 * fs                 # Frecuencia de Nyquist
    normal_cutoff = np.array(cutoff) / nyq
    b, a = butter(order, normal_cutoff, btype=btype, analog=False) #butter para obtener los coeficientes del filtro digital
    y = lfilter(b, a, data)
    return y

# Parámetros del filtro, 6 da una transición mas abrupta pero puede ser mas inestable
order = 6

# Filtro pasa bajos deja pasar la señal de 10Hz
low_cutoff = 30  # Hz
y_low = butter_filter(x, low_cutoff, fs, order, btype='low')

# Filtro pasa altos deja pasar la señal de 40 y 120 Hz
high_cutoff = 30  # Hz
y_high = butter_filter(x, high_cutoff, fs, order, btype='high')

# Filtro pasa bandas deja pasar la señal de 40Hz
band_cutoff = [20, 100]  # Hz
y_band = butter_filter(x, band_cutoff, fs, order, btype='band')

# Mostrar gráficas se usan subplots para comparar visualmente cada filtro
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, x)
plt.title('Señal original (10 Hz + 40 Hz + 120 Hz)')
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(t, y_low)
plt.title('Filtro Pasa Bajos (<30 Hz)')
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(t, y_high)
plt.title('Filtro Pasa Altos (>30 Hz)')
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t, y_band)
plt.title('Filtro Pasa Bandas (20-100 Hz)')
plt.grid()

plt.tight_layout()
plt.show()