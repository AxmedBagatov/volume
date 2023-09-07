import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

SAMPLE_RATE = 44100
DURATION = 5

def generate(freq, sample_rate, duration):
    x = np.linspace(0,duration, sample_rate*duration, endpoint=False)
    frequences = x * freq
    y = np.sin(2*np.pi*frequences)
    return x, y

#x, y = generate(2, SAMPLE_RATE, DURATION)
#plt.plot(x, y)
#plt.show()

_, nice_tone = generate(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate(4000, SAMPLE_RATE, DURATION)

noise_tone = noise_tone * 0.3
mixed_tone = nice_tone + noise_tone
normalize_tone = np.int16((mixed_tone/mixed_tone.max())*32767)

from scipy.fft import rfft, rfftfreq
N = SAMPLE_RATE*DURATION
yf = rfft(normalize_tone)
xf = rfftfreq(N,1/SAMPLE_RATE)
#plt.plot(xf,np.abs(yf))

points = len(xf) / (SAMPLE_RATE/2)
target = int(points*4000)
yf[target-2:target+2]=0

from scipy.fft import irfft

new_signal = irfft(yf)
plt.plot(new_signal[:1000])

#plt.plot(xf,np.abs(yf))
#plt.plot(normalize_tone[:1000])
plt.show()