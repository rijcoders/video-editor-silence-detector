
from moviepy.editor import AudioFileClip

def extract_audio():
    audio = AudioFileClip("7.mp4")
    audio.write_audiofile("7.mp3", 44100)  # fps


if __name__ == '__main__':
    extract_audio()