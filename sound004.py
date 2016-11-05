import numpy as np
import wave
import sys
import math
import contextlib

import scipy
import scipy.io.wavfile as wavfile

fname = 'test_speak.wav'
outname = 'filtered004.wav'

rate, data = wavfile.read(fname)

wave_in_freq_domain = scipy.fft(data)

print(wave_in_freq_domain[:5])

minimum = 100000

for i in range(len(wave_in_freq_domain[:])):
    for j in np.absolute(wave_in_freq_domain[i]):
        if j < minimum:
            if minimum < 10:
                pass
            else:
                minimum = j
            # wave_in_freq_domain[i] = 0

print(minimum)

