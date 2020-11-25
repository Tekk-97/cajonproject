import pyaudio
import numpy as np
import peakpicking as pp

print(pyaudio.get_portaudio_version())

CHUNK = 2 ** 8
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                frames_per_buffer=CHUNK, input_device_index=1)



sample_list=[0] *100
pclass= pp.real_time_peak_detection(sample_list,30,100,0.5)
#윈도우사이즈,임계값,영향값

while (True):
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    if(pclass.thresholding_algo(int(np.average(np.abs(data))))==1):
        print(np.average(np.abs(data)))


stream.stop_stream()
stream.close()
p.terminate()
