# main.py

from translator.speech_recognition import SpeechRecognizer
from translator.language_translation import LanguageTranslator
from translator.speech_synthesis import SpeechSynthesizer

def main():
    source_language = 'en-US'
    target_language = 'fr'

    recognizer = SpeechRecognizer(language=source_language, model_path='models/vosk-model-small-en-us-0.15')
    translator = LanguageTranslator(dest_language=target_language)
    synthesizer = SpeechSynthesizer(language=target_language[:2])  # 'fr'

    while True:
        speech_text = recognizer.capture_speech()
        if speech_text.lower() in ['exit', 'quit', 'stop']:
            print("Exiting the translator.")
            break
        if speech_text:
            translated_text = translator.translate_text(speech_text)
            synthesizer.speak_text(translated_text)

if __name__ == "__main__":
    main()
