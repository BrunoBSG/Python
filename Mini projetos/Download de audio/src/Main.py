from downloader import Downloader
from audio_extractor import AudioExtractor
import os

def main():

    print("=" * 50)
    print("AutoShorts")
    print("=" * 50)

    url = input("Cole a URL do vídeo: ")

    downloader = Downloader()

    video_path = downloader.download(url)

    audio_extrator = AudioExtractor()

    audio_path = audio_extrator.extract(video_path)

    
    print(f"Áudio: {audio_path}")
    
    os.remove(video_path)


if __name__ == "__main__":
    main()