import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

wav=wave.open("test.wav","r")

raw=wav.readframes(-1)
raw=np.frombuffer(raw)

if wav.getnchannels()== 2:
    print("Stereo files are not supported")
    sys.exit(0)
##Time= np.linespace(0, len(raw) / fs, num=len(raw))

plt.title("Waveform of Wave FIle")

plt.plot(raw)

plt.ylabel("Amplitude")

plt.show()
