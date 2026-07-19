from downloader import Downloader
from audio_extractor import AudioExtractor


def main():

    print("=" * 50)
    print("AutoShorts")
    print("=" * 50)

    url = input("Cole a URL do vídeo: ")

    downloader = Downloader()

    video_path = downloader.download(url)

    audio_extrator = AudioExtractor()

    audio_path = audio_extrator.extract()

    print("\nVídeo:")
    print(video_path)




if __name__ == "__main__":
    main()