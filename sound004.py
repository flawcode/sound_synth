import numpy as np
import wave
import sys
import math
import contextlib

import scipy
import scipy.io.wavfile as wavfile

fname = 'test_speak.wav'
outname = 'filtered004_004.wav'
noise_amp_attenuation = 10000

rate, data = wavfile.read(fname)

print(data[:5])

wave_in_freq_domain = scipy.fft(data)

print(wave_in_freq_domain[:5])

for a, freq in enumerate(wave_in_freq_domain):
    for b, absolute_val in enumerate(np.absolute(freq)):
        if absolute_val < noise_amp_attenuation:
            wave_in_freq_domain[a][b] = 0

wave_in_time_domain = scipy.ifft(wave_in_freq_domain)

wave_in_time_domain_mod = data
how_many_zeros = 0
printed = False
for i, w in enumerate(wave_in_time_domain):
    if any(w.real) == 0:
        how_many_zeros += 1
    if how_many_zeros == 2 and not printed:
        print("one such index:", i)
        print("one such index:", w)
        print("prev val", wave_in_time_domain_mod[i])
        print("adjacent valuie", wave_in_time_domain_mod[i+1])
        printed = True
    wave_in_time_domain_mod[i] = w.real

print(how_many_zeros)

print(wave_in_time_domain_mod[:5])

print(wave_in_time_domain_mod[21038])
print(wave_in_time_domain_mod[21039])
print(wave_in_time_domain_mod[21037])

wavfile.write(outname, 44100, wave_in_time_domain_mod)
