import pyaudio
import numpy as np
import peakpicking as pp
import play_music
import play_short_sound
from multiprocessing import Process


music_path = 'music.wav'

if __name__ == '__main__':
    CHUNK = 2 ** 8
    RATE = 44100

    p = pyaudio.PyAudio()


    Process(target=play_music.play_music).start()




    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK, input_device_index=1)



    sample_list=[0] *100
    pclass= pp.real_time_peak_detection(sample_list,30,100,0.5)
    #윈도우사이즈,임계값,영향값

    while (True):
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)

        if(pclass.thresholding_algo(int(np.average(np.abs(data))))==1):
            Process(target=play_short_sound.play_music).start()
            print(np.average(np.abs(data)))


    stream.stop_stream()
    stream.close()
    p.terminate()
