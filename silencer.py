from pydub import AudioSegment,silence

myaudio = intro = AudioSegment.from_mp3("test.mp3")
dBFS=myaudio.dBFS
silence = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=dBFS-16)

silence = [((start/1000),(stop/1000)) for start,stop in silence] #in sec