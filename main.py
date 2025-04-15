import whisper
import os
import subprocess
from constants import MODEL_ROOT, AUDIO_ROOT, OUTPUT_ROOT, LANGUAGE, Model


def main(model_name: Model, file_name: str):
    subprocess.run(
        [
            "whisper",
            AUDIO_ROOT + "/" + file_name,
            "--model",
            model_name,
            "--model_dir",
            MODEL_ROOT,
            "--output_dir",
            OUTPUT_ROOT,
            "--language",
            LANGUAGE,
        ]
    )

    # Remove the redundant text files after processing
    for i in os.listdir(OUTPUT_ROOT):
        if i.endswith(".json") or i.endswith(".tsv"):
            os.remove(os.path.join(OUTPUT_ROOT, i))
