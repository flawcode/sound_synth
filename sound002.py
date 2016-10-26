from math import sin, pi
import wave
import struct

N = 168
x = range(N)
y = N * [0]

for i in x:
    y1 = 4 / pi*sin(2*pi*i/N)
    y2 = 4 / (3*pi)*sin(6*pi*i/N)
    y3 = 4 / (5*pi)*sin(10*pi*i/N)
    y[i] = y1 + y2 + y3

y = 1313*y
x = range(1313*N)

fout = wave.open("sin1313.wav", "w")
fout.setnchannels(1)
fout.setsampwidth(2)
fout.setframerate(44100)
fout.setcomptype("NONE", "Not Compressed")
BinStr = b""
for i in range(len(y)):
    BinStr = BinStr + struct.pack("h", round(y[i]*20000))

fout.writeframesraw(BinStr)
fout.close()
