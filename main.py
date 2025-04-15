import json
import os
import subprocess
from constants import MODEL_ROOT, AUDIO_ROOT, OUTPUT_ROOT, LANGUAGE, CACHE_FILE


def main():
    with open(CACHE_FILE) as f:
        config = json.load(f)
    model_name = config["model_name"]
    file_name = config["file_name"]

    if not os.path.exists(AUDIO_ROOT):
        os.makedirs(AUDIO_ROOT)
    if not os.path.exists(OUTPUT_ROOT):
        os.makedirs(OUTPUT_ROOT)
    if not os.path.exists(MODEL_ROOT):
        os.makedirs(MODEL_ROOT)
    # Check if the audio file exists
    audio_file_path = os.path.join(AUDIO_ROOT, file_name)

    if not os.path.exists(audio_file_path):
        print(f"Audio file {file_name} does not exist in {AUDIO_ROOT}.")
        return

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


if __name__ == "__main__":
    main()
