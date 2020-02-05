
##test_sound2vec

from sound2vec import Sound2VecModel
import os

PATH_TEST_1 = os.path.normpath(os.path.join(os.path.abspath(''), 'audio/test1.wav'))
PATH_TEST_2 = os.path.normpath(os.path.join(os.path.abspath(''), 'audio/test2.wav'))
PATH_TEST_3 = os.path.normpath(os.path.join(os.path.abspath(''), 'audio/test3.wav'))

audio_sound2vec = Sound2VecModel(PATH_TEST_1)
print(audio_sound2vec)

audio_sound2vec = Sound2VecModel(PATH_TEST_2)
print(audio_sound2vec)

audio_sound2vec = Sound2VecModel(PATH_TEST_3)
print(audio_sound2vec)



