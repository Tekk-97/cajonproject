import pyaudio
import wave

chunk = 1024

path = 'music.wav'


with wave.open(path,'rb') as f:
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)

    date = f.readframes(chunk)
    while date:
        stream.write(date)
        date=f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()