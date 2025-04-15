from dataclasses import dataclass

MODEL_ROOT = "/app/models"
AUDIO_ROOT = "/app/audios"
OUTPUT_ROOT = "/app/outputs"
LANGUAGE = "Chinese"  # Chinese, English


@dataclass
class Model:
    # tiny, base, small, medium, large
    tiny: str = "tiny"
    base: str = "base"
    small: str = "small"
    medium: str = "medium"
    large: str = "large"
