from utils import speech_to_text, get_volume_times, otnosh, get_monotone
from audio_classification import is_speech
from record import recording

THRESHOLD_LOW = 100
THRESHOLD_LOUD = 100000
THRESHOLD_MONOTONE = 1000
THRESHOLD_SILENSE = 10


class Sound2VecModel:
    def __init__(self, audio_path):
        self.is_speech = is_speech(audio_path)
        try:
            if self.is_speech:
                print('* ЗАПИСЬ ЯВЛЯЕТСЯ ЗВУКОМ')
                print(self.get_volume(audio_path))
                self.volume = self.get_volume(audio_path)
                print('Громкость: ', self.volume)
                self.silens_segm = self.get_silens_segm(audio_path)
                print('Сегменты: ', self.silens_segm)
                self.monotone = self.get_monotone(audio_path)
                print('Монотонность: ', self.monotone)
                self.text = self.get_text(audio_path)
                print('ТЕКСТ: ', self.text)
                self.result = 'Получен вектор с параметрами: '

            else:
                self.result = 'Аудио файл не сожержит речь!'
        except Exception as e:
            self.result = e

    def __str__(self):
        if self.is_speech:
            return f'{self.result} {self.volume} {self.silens_segm} {self.monotone} {self.text}'
        else:
            return f'{self.result}'

    def get_volume(self, audio_path):
        print('OL')
        print(get_volume_times(audio_path))
        return 'Громкость'

    def get_silens_segm(self, audio_path):
        return otnosh(audio_path, THRESHOLD_SILENSE = 10)

    def get_monotone(self, audio_path):
        return get_monotone(audio_path, THRESHOLD_MONOTONE)

    def get_text(self, audio_path):

        return speech_to_text(audio_path)

    def get_json(self):
        pass

    def get_recomend(self):
        pass

test_path = 'audio/test1.wav'
if __name__ == "__main__":
    sound = Sound2VecModel('test1.wav')
    #print(sound)
    #sound.get_text()
