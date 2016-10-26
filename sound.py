import scipy.io.wavfile as wavfile

rate, data = wavfile.read("answer.wav")

print(data[:5])
