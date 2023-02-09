from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import pyaudio

def speak(text ,lang="ko", speed=False):
    tts = gTTS(text=text, lang=lang , slow=speed)
    tts.save("./tts.mp3")
    #os.system("afplay " + "./tts.mp3")
    #playsound.playsound("C:\\Users\\yoolim\\PycharmProjects\\forder\\tts.mp3")

try:
    while True:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('음성을 입력하세요.')
            audio = r.listen(source)
            try:
                stt = r.recognize_google(audio, language='ko-KR')
                print('음성변환 : ' + stt)

                if '시리' in stt:
                    speak('네, 안녕하세요')
                    print('네, 안녕하세요')

            except sr.UnknownValueError:
                print('오디오를 이해할 수 없습니다.')
            except sr.RequestError as e:
                print(f'에러가 발생하였습니다. 에러원인 : {e}')

except KeyboardInterrupt:
    pass