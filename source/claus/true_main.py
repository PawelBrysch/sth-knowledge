from gtts import gTTS
tts = gTTS('Das ferkelchen', lang='de')
tts.save('hello.mp3')