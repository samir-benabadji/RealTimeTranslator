# translator/speech_synthesis.py

from gtts import gTTS
import os
import uuid
from utils.audio_player import play_audio

class SpeechSynthesizer:
    def __init__(self, language='fr'):
        self.language = language

    def speak_text(self, text):
        try:
            tts = gTTS(text=text, lang=self.language)
            filename = f"temp_audio_{uuid.uuid4()}.mp3"
            tts.save(filename)
            play_audio(filename)
            os.remove(filename)
        except Exception as e:
            print(f"Speech synthesis error: {e}")
