from pathlib import Path
from moviepy import VideoFileClip


class AudioExtractor:

    def extract(self, video_path: str) -> str:
        """
        Extrai o áudio do vídeo e salva como MP3.

        Retorna o caminho do áudio.
        """

        video_path = Path(video_path)

        audio_path = video_path.parent / "audio.mp3"

        print("\nExtraindo áudio...")

        video = VideoFileClip(str(video_path))

        video.audio.write_audiofile(
            str(audio_path),
            codec="mp3"
        )

        video.close()

        print("Áudio extraído!")

        return str(audio_path)