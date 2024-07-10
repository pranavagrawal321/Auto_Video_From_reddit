import pyttsx3
import os

voiceoverDir = "Voiceovers"


def create_voice_over(fileName, text, voice=None, rate=None, volume=None):
    try:
        os.makedirs(voiceoverDir, exist_ok=True)

        filePath = os.path.join(voiceoverDir, f"{fileName}.mp3")

        engine = pyttsx3.init()

        if voice:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[voice].id)

        if rate:
            engine.setProperty('rate', rate)

        if volume:
            engine.setProperty('volume', volume)

        engine.save_to_file(text, filePath)
        engine.runAndWait()

        return filePath

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    create_voice_over('test_custom', 'This is a custom voiceover', voice=1, rate=150, volume=0.9)
