import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, rfft, fftshift

def signal_am(amp=1.0, km=0.25, fc=10.0, fs=2.0, period=100):
    tt = 2.0 * np.pi * np.linspace(0, 1, period)
    return amp * (1 + km * np.cos(fs * tt)) * np.cos(fc * tt)

N = 1024
# Create AM-signal
fs = 15 # Modulation frequency
fc = [20, 45, 60] # Carrier frequency
sig = [signal_am(amp=1.0, km=0.45, fc=i, fs=fs, period=N) for i in fc]
# Calculate FFT
sft = np.abs(rfft(sig, axis=1)) / N / 0.5
plt.figure(figsize=(12, 6), dpi=80)
for i, freq in enumerate(fc):
    plt.subplot(len(fc), 2, 2*i+1)
    if i == 0:
        plt.title('AM-signal')
    plt.plot(sig[i])
    plt.xlim([0, N-1])
    plt.grid(True)
    plt.subplot(len(fc), 2, 2*i+2)
    if i == 0:
        plt.title('Spectrum')
    plt.plot(sft[i])
    plt.xlim([0, N//2-1])
    plt.grid(True)
plt.show()