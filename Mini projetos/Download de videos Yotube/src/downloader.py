from pathlib import Path
from yt_dlp import YoutubeDL


class Downloader:
    def __init__(self):
        # Caminho da pasta de downloads
        self.download_folder = Path(__file__).parent.parent / "downloads"

        # Cria a pasta caso ela não exista
        self.download_folder.mkdir(exist_ok=True)

    def download(self, url: str) -> str:
        """
        Baixa um vídeo do YouTube e retorna o caminho do arquivo.
        """

        options = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": str(self.download_folder / "%(title)s.%(ext)s"),
            "noplaylist": True
        }

        print("\nBaixando vídeo...")

        with YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)

            filename = ydl.prepare_filename(info)

            # Caso o vídeo seja convertido para MP4
            filename = str(Path(filename).with_suffix(".mp4"))

        print("Download concluído!")

        return filename