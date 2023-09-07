import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, rfft, fftshift

def signal_fm(amp=1.0, kd=0.25, fc=10.0, fs=2.0, period=100):
    tt = 2.0 * np.pi * np.linspace(0, 1, period)
    return amp * np.cos(fc * tt + kd/fs * np.sin(fs * tt))


N = 512
sig = signal_fm(amp=1.0, kd=15, fc=40, fs=4, period=N)
smd = np.sin(4 * 2.0 * np.pi * np.linspace(0, 1, N))
plt.figure(figsize=(12, 6), dpi=80)
plt.subplot(2, 1, 1)
plt.title('Modulation signal')
plt.plot(smd)
plt.xlim([0, N//2-1])
plt.grid(True)
plt.subplot(2, 1, 2)
plt.title('FM-signal')
plt.plot(sig)
plt.xlim([0, N//2-1])
plt.grid(True)
plt.show()