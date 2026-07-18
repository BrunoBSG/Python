from pathlib import Path
from yt_dlp import YoutubeDL
import json


class Downloader:

    def __init__(self):

        # AutoShorts/
        self.project_root = Path(__file__).resolve().parent.parent.parent

        # AutoShorts/downloads
        self.download_folder = self.project_root / "downloads"

        self.download_folder.mkdir(exist_ok=True)

    def download(self, url: str) -> str:
        """
        Baixa um vídeo do YouTube.

        Retorna o caminho do video.mp4
        """

        print("\nObtendo informações do vídeo...")

        # Obtém apenas as informações do vídeo
        with YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)

        video_id = info["id"]

        # Cria uma pasta para o vídeo
        video_folder = self.download_folder / video_id
        video_folder.mkdir(exist_ok=True)

        options = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": str(video_folder / "video.%(ext)s"),
            "noplaylist": True,
            "writesubtitles": False,
            "writeautomaticsub": False,
        }

        print("Baixando vídeo...")

        with YoutubeDL(options) as ydl:
            ydl.download([url])

        # Salva as informações do vídeo
        info_file = video_folder / "info.json"

        with open(info_file, "w", encoding="utf-8") as file:
            json.dump(
                info,
                file,
                ensure_ascii=False,
                indent=4
            )

        video_path = video_folder / "video.mp4"

        print("Download concluído!")

        return str(video_path)