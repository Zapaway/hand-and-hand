class TTS:

    def __init__(self):
        import os
        from dotenv import load_dotenv

        load_dotenv()

        string = ""
        self.DEEPGRAM_URL = "https://api.deepgram.com/v1/speak?model=aura-luna-en"
        self.DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
        self.SPEAK_OPTIONS = {"text": string}

    def play_streaming_audio(self, stream):
        import io
        from pydub import AudioSegment
        import sounddevice as sd
        import numpy as np

        try:
            audio_data = io.BytesIO()
            for chunk in stream.iter_content(chunk_size=1024):
                if chunk:
                    audio_data.write(chunk)
            audio_data.seek(0)

            audio_segment = AudioSegment.from_file(audio_data)
            audio_array = np.array(audio_segment.get_array_of_samples())
            sample_rate = audio_segment.frame_rate

            sd.play(audio_array, samplerate=sample_rate)
            sd.wait()

        except Exception as e:
            print(f"Error playing sound: {e}")

    def tts(self, text: str):
        import requests

        try:
            self.SPEAK_OPTIONS["text"] = text
            headers = {
                "Authorization": f"Token {self.DEEPGRAM_API_KEY}",
                "Content-Type": "application/json",
            }

            response = requests.post(
                self.DEEPGRAM_URL, headers=headers, json=self.SPEAK_OPTIONS, stream=True
            )
            response.raise_for_status()

            self.play_streaming_audio(response)

        except Exception as e:
            print(f"Exception: {e}")


if __name__ == "__main__":
    t = TTS()
    t.tts("erm, I dont mean to brag but it sounds like a windows issue")
