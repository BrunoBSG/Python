import json
from pathlib import Path

from faster_whisper import WhisperModel


class Transcriber:

    def __init__(self, model_size: str = "base"):
        """
        Modelos disponíveis:
        tiny
        base
        small
        medium
        large-v3

        Recomendo começar com 'base'.
        """

        print("Carregando modelo Whisper...")

        self.model = WhisperModel(
            model_size,
            device="cpu",
            compute_type="int8"
        )

    def transcribe(self, audio_path: str):

        audio_path = Path(audio_path)

        output_folder = audio_path.parent

        transcript_file = output_folder / "transcript.txt"
        subtitle_file = output_folder / "subtitles.srt"
        segments_file = output_folder / "segments.json"

        print("\nTranscrevendo áudio...")

        segments, info = self.model.transcribe(
            str(audio_path),
            language="pt",
            beam_size=5
        )

        transcript = ""
        json_segments = []

        with open(subtitle_file, "w", encoding="utf-8") as srt:

            for index, segment in enumerate(segments, start=1):

                transcript += segment.text.strip() + "\n"

                json_segments.append({
                    "start": segment.start,
                    "end": segment.end,
                    "text": segment.text.strip()
                })

                srt.write(f"{index}\n")
                srt.write(
                    f"{self._format_time(segment.start)} --> "
                    f"{self._format_time(segment.end)}\n"
                )
                srt.write(segment.text.strip() + "\n\n")

        with open(transcript_file, "w", encoding="utf-8") as txt:
            txt.write(transcript)

        with open(segments_file, "w", encoding="utf-8") as js:
            json.dump(
                json_segments,
                js,
                indent=4,
                ensure_ascii=False
            )

        print("Transcrição concluída!")

        return json_segments

    def _format_time(self, seconds: float):

        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        milliseconds = int((seconds - int(seconds)) * 1000)

        return (
            f"{hours:02}:{minutes:02}:{secs:02},"
            f"{milliseconds:03}"
        )