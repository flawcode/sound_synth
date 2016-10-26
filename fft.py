"""
filter out the noise
"""
import numpy as np
from scipy.signal import freqz
from scipy.signal import butter, lfilter
import scipy.io.wavfile as wavfile


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def read_wav_file(wave_file):
    return wavfile.read(wave_file)


if __name__ == "__main__":

    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 5000.0

    # telephony system standard of 300Hz to 3.4kHz
    lowcut = 300
    highcut = 3400

    # Filter a noisy signal.
    rate, data = wavfile.read("test_speak.wav")
    data_ch1 = data[:, 0]
    print(data_ch1[:5])
    print(rate)

    y = butter_bandpass_filter(data_ch1, lowcut, highcut, fs, order=6)


    wavfile.write("out.wav", 44100, y)
