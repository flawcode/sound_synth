"""
writing a wav file with numpy and scipy
"""

import numpy as np
import scipy.io.wavfile as wavfile

N = 168
x = np.arange(N)
y = 4 / np.pi*np.sin(2*np.pi*x/N)
y += 4 / (3*np.pi)*np.sin(6*np.pi*x/N)
y += 4 / (5*np.pi)*np.sin(10*np.pi*x/N)

y = np.tile(y, 1313)
y = y/max(y)
wavfile.write("sqwvfile.wav", 44100, y)
