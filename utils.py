import librosa
import os
import wave
import struct
import pyAudioAnalysis
import speech_recognition as sr
import time

#path = os.path.join(os.path.abspath(''), '9500a1ef1441.mp3')
#wav, sr = librosa.load(path, mono=True, sr=target_sr)

def get_volume_times(wav_path, threshold=100000, threshold_low=100, time_constant=0.1):
    wav = wave.open(wav_path, 'r')

    length = wav.getnframes()
    samplerate = wav.getframerate()

    assert wav.getnchannels() == 1, 'wav must be mono'
    assert wav.getsampwidth() == 2, 'wav must be 16-bit'


    is_loud = False
    is_low = False
    result = [(0., is_loud)]

    mean = 0
    variance = 0

    alpha = 1 / (time_constant * float(samplerate))

    for i in range(length):
        sample_time = float(i) / samplerate
        sample = struct.unpack('<h', wav.readframes(1))
        sample = sample[0]
        mean = (1 - alpha) * mean + alpha * sample
        variance = (1 - alpha) * variance + alpha * (sample - mean) ** 2

        new_is_loud = variance > threshold
        new_is_low = variance < threshold_low

        if is_low != new_is_low:
            result.append((sample_time, new_is_loud, 'LOW'))
        if is_loud != new_is_loud:
            result.append((sample_time, new_is_loud, 'LOUD'))

        is_low = new_is_low
        is_loud = new_is_loud

    return result

def speech_to_text(wav_path):
        try:

            wav = wave.open(wav_path, 'r')
            length = wav.getnframes()
            rate = wav.getframerate()
            duration = length / float(rate)

            # print('длительность', duration)

            rec = sr.Recognizer()
            harvard = sr.AudioFile(wav_path)
            with harvard as source:
                audio = rec.record(source)
            text = rec.recognize_google(audio, language="ru_RU")
            if len(text) > 0:
                list_txt = text.split()
                myset = set(list_txt)
                tempo = len(myset) / duration
                print('Длина списка:', len(myset), ' Длительность: ', duration, 'ТЕМП =', tempo)
                return len(myset), myset, tempo
            else:
                return 0
        except Exception as e:
            print(e)



def otnosh(wav_path, THRESHOLD_SILENSE = 10, time_constant=0.1):
    wav = wave.open(wav_path, 'r')
    length = wav.getnframes()
    samplerate = wav.getframerate()

    assert wav.getnchannels() == 1, 'wav must be mono'
    assert wav.getsampwidth() == 2, 'wav must be 16-bit'

    bin = []

    mean = 0
    variance = 0

    alpha = 1 / (time_constant * float(samplerate))

    for i in range(length):
        sample_time = float(i) / samplerate
        sample = struct.unpack('<h', wav.readframes(1))
        sample = sample[0]
        mean = (1 - alpha) * mean + alpha * sample
        variance = (1 - alpha) * variance + alpha * (sample - mean) ** 2

        if variance > THRESHOLD_SILENSE:
            bin.append(1)
        else:
            bin.append(0)

    res = bin.count(0) / bin.count(1)
    return res

def get_monotone(wav_path, THRESHOLD_MONOTONE = 10, time_constant=0.1):
    wav = wave.open(wav_path, 'r')
    length = wav.getnframes()
    samplerate = wav.getframerate()

    assert wav.getnchannels() == 1, 'wav must be mono'
    assert wav.getsampwidth() == 2, 'wav must be 16-bit'

    bin = []

    mean = 0
    variance = 0

    alpha = 1 / (time_constant * float(samplerate))

    for i in range(length):
        sample_time = float(i) / samplerate
        sample = struct.unpack('<h', wav.readframes(1))
        sample = sample[0]
        mean = (1 - alpha) * mean + alpha * sample
        variance = (1 - alpha) * variance + alpha * (sample - mean) ** 2

        if variance > THRESHOLD_MONOTONE:
            bin.append(1)
        else:
            bin.append(0)
    res = bin.count(0) / bin.count(1)
    return res



