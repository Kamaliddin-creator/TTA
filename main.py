from gtts import gTTS

audio = 'audio.mp3'
language = 'ru'
sp = gTTS(text='Короче я дебилка и не могу самостоятельно какать. Меня зовут татьяна!', lang=language, slow=False)

sp.save(audio)