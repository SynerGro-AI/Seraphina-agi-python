"""
Voice interaction module for Seraphina AGI Companion
Provides text-to-speech and speech-to-text functionality.
"""

import pyttsx3
import speech_recognition as sr

def speak(text: str, language: str = 'en-US') -> None:
    """
    Convert text to speech using pyttsx3.

    Args:
        text: The text to speak
        language: Language code (currently not used, defaults to system default)
    """
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech synthesis error: {e}")

def listen(timeout: int = 5) -> str:
    """
    Listen for speech and convert to text using speech_recognition.

    Args:
        timeout: Maximum time to listen for speech in seconds

    Returns:
        The recognized text, or empty string if recognition failed
    """
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=timeout)
            text = recognizer.recognize_google(audio)
            return text
    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
        return ""
    except Exception as e:
        print(f"Microphone error: {e}")
        return ""