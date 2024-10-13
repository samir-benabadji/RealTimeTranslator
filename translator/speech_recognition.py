# translator/speech_recognition.py

import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

class SpeechRecognizer:
    def __init__(self, language='en-US', model_path='models/vosk-model-small-en-us-0.15'):
        self.language = language
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.q = queue.Queue()

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status, flush=True)
        self.q.put(bytes(indata))

    def capture_speech(self):
        print("Please speak... (say 'exit' to quit)")

        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=self.audio_callback):
            while True:
                data = self.q.get()
                if self.recognizer.AcceptWaveform(data):
                    result = self.recognizer.Result()
                    text = json.loads(result)['text']
                    if text:
                        print(f"You said: {text}")
                        if 'exit' in text.lower():
                            return 'exit'
                        return text
                else:
                    pass
