from pyt2s.services import stream_elements
import os
import logging

voiceover_dir = "Voiceovers"
question_dir = os.path.join(voiceover_dir, "Questions")
answer_dir = os.path.join(voiceover_dir, "Answers")
os.makedirs(question_dir, exist_ok=True)
os.makedirs(answer_dir, exist_ok=True)


def create_voiceover(text, filename):
    data = stream_elements.requestTTS(text, stream_elements.Voice.Russell.value)

    with open(f"Voiceovers/{filename}.mp3", '+wb') as file:
        file.write(data)

    print(f"Voice saved to Voiceovers/{filename}.mp3")


if __name__ == '__main__':
    create_voiceover("Hey this is a test voiceover", 'test')