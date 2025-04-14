import whisper
import os
import subprocess

MODEL_ROOT = "/app/models"
AUDIO_ROOT = "/app/audios"
OUTPUT_ROOT = "/app/outputs"
AUDIO_FILE = "test.mp3"
MODLE_NAME = "small"  # tiny, base, small, medium, large
LANGUAGE = "Chinese"  # Chinese, English

subprocess.run(
    [
        "whisper",
        AUDIO_ROOT + "/" + AUDIO_FILE,
        "--model",
        MODLE_NAME,
        "--model_dir",
        MODEL_ROOT,
        "--output_dir",
        OUTPUT_ROOT,
        "--language",
        LANGUAGE,
    ]
)
