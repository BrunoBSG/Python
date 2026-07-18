from services.downloader import Downloader
from services.audio_extractor import AudioExtractor
from services.transcriber import Transcriber
from services.ai.ai_provider import AIProvider


def main():
    provider = AIProvider.create()
    print("Testando Gemini...")
    print(provider.test_connection())
    
    print("=" * 50)
    print("             AutoShorts")
    print("=" * 50)
     
    url = input("Cole a URL do vídeo: ").strip()

    if not url:
        print("URL inválida!")
        return

    try:
        # ===========================
        # Download
        # ===========================
        downloader = Downloader()
        video_path = downloader.download(url)

        # ===========================
        # Extração do áudio
        # ===========================
        extractor = AudioExtractor()
        audio_path = extractor.extract(video_path)

        # ===========================
        # Transcrição
        # ===========================
        transcriber = Transcriber()
        segments = transcriber.transcribe(audio_path)

        print("\n" + "=" * 50)
        print("Processo concluído com sucesso!")
        print("=" * 50)

        print(f"Vídeo: {video_path}")
        print(f"Áudio: {audio_path}")
        print(f"Segmentos encontrados: {len(segments)}")

    except Exception as erro:
        print(f"\nOcorreu um erro: {erro}")


if __name__ == "__main__":
    main()