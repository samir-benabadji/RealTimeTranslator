# utils/audio_player.py

from playsound import playsound
import platform

def play_audio(file_path):
    try:
        playsound(file_path)
    except Exception as e:
        print(f"Audio playback error: {e}")
