import json
import os
from constants import USER_CACHE_FILE


class CacheOperations:
    def __init__(self):
        self.cache_file = USER_CACHE_FILE

        # Ensure the cache file exists
        if not os.path.exists(self.cache_file) or os.path.getsize(self.cache_file) == 0:
            self.init_empty_cache()

    def init_empty_cache(self):
        with open(self.cache_file, "w") as f:
            json.dump({"file_name": "", "model_name": ""}, f)

    def __read(self) -> dict | None:
        if not os.path.exists(self.cache_file):
            self.init_empty_cache()

        with open(self.cache_file, "r") as f:
            config = json.load(f)
        return config

    def __save(self, key: str, value: str):
        config = self.__read()
        config[key] = value
        with open(self.cache_file, "w") as f:
            json.dump(config, f)

    def read_audio_file_name(self) -> str | None:
        config = self.__read()
        return config["file_name"] if config["file_name"] else None

    def read_model_name(self) -> str | None:
        config = self.__read()
        return config["model_name"] if config["model_name"] else None

    def save_audio_file_name(self, file_name: str):
        self.__save("file_name", file_name)

    def save_model_name(self, model_name: str):
        self.__save("model_name", model_name)
