#from pyAudioAnalysis import audioBasicIO
#from pyAudioAnalysis import audioFeatureExtraction

def get_features(audio_path):
    [Fs, x] = audioBasicIO.readAudioFile("file.wav")
    F, f_names = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
    return F, f_names

def is_speech(audio_path):
    #print(get_features(audio_path))
    return True

