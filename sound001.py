# commands to read the first few samples

import struct
import wave
wrd = wave.open("answer.wav", "r")
S1String = wrd.readframes(1)
S1 = struct.unpack("h", S1String)
print(S1[0])

S2String = wrd.readframes(1)
S2 = struct.unpack("h", S2String)
print(S2[0])

S3String = wrd.readframes(1)
S3 = struct.unpack("h", S3String)
print(S3)
(4,)

print(struct.unpack("h", wrd.readframes(1)))
print(struct.unpack("h", wrd.readframes(1)))
print(struct.unpack("h", wrd.readframes(1)))
print(struct.unpack("h", wrd.readframes(1)))

#>>> struct.unpack("h", wrd.readframes(1))
#(-1,)
#>>> struct.unpack("h", wrd.readframes(1))
#(-13,)
#>>> struct.unpack("h", wrd.readframes(1))
#(14,)
#>>> struct.unpack("h", wrd.readframes(1))
#(12,)
#>>> struct.unpack("h", wrd.readframes(1))
#(-1,)

