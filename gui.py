import os
import shutil
import subprocess
import tkinter as tk

from tkinter import filedialog, messagebox, ttk
from cache import CacheOperations
from constants import USER_AUDIO_DIR, USER_OUTPUT_DIR, MODELS


class WhisperGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Whisper Docker Interface")
        self.geometry("600x400")
        self.cache = CacheOperations()

        # read from cache, and set default values

        self.model_var = tk.StringVar(value=self.cache.read_model_name())
        self.audio_var = tk.StringVar(value=self.cache.read_audio_file_name())

        # create windows
        self.create_widgets()

    def create_widgets(self):
        # Title label
        tk.Label(self, text="Whisper Docker Interface", font=("Arial", 24)).pack(
            pady=20
        )

        # Audio selection
        tk.Label(self, text="Select Audio File:").pack()
        files = self.get_audio_files()
        self.audio_combo = ttk.Combobox(self, textvariable=self.audio_var, values=files)
        self.audio_combo.pack(fill="x", padx=20)

        # Model selection
        tk.Label(self, text="Select Model:").pack()
        model_combo = ttk.Combobox(self, textvariable=self.model_var, values=MODELS)
        model_combo.pack(fill="x", padx=20)

        # Button frame
        frame = tk.Frame(self)
        frame.pack(pady=10)

        # Run docker build
        tk.Button(frame, text="Build image", command=self.build_image).pack(
            side=tk.LEFT, pady=10
        )

        # Run main script
        tk.Button(frame, text="Run whisper", command=self.run).pack(
            side=tk.LEFT, pady=10
        )

        # Stop docker container
        tk.Button(frame, text="Stop whisper", command=self.stop).pack(
            side=tk.LEFT, pady=10
        )

        # Upload
        tk.Button(frame, text="Upload Audio", command=self.upload_audio).pack(
            side=tk.LEFT, pady=5
        )

    def upload_audio(self):
        path = filedialog.askopenfilename(
            filetypes=[("Audio files", "*.mp3 *.mp4 *.wav")]
        )
        if not path:
            return
        shutil.copy(path, USER_AUDIO_DIR)
        messagebox.showinfo("Uploaded", f"{os.path.basename(path)} uploaded")
        self.refresh_lists()

    def get_audio_files(self):
        files = os.listdir(USER_AUDIO_DIR)
        return [f for f in files if f.endswith((".mp3", ".mp4", ".wav"))]

    def delete_files(self, folder: str, file_name: str):
        file_path = os.path.join(folder, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            messagebox.showinfo("Deleted", f"{file_name} deleted")
        else:
            messagebox.showerror("Error", f"{file_name} not found")

    def build_image(self):
        subprocess.run(["docker-compose", "build"], check=False)
        messagebox.showinfo("built", "Docker image built")

    def run(self):
        audio_file = self.audio_var.get()
        model = self.model_var.get()

        self.cache.save_audio_file_name(audio_file)
        self.cache.save_model_name(model)

        if not audio_file:
            messagebox.showerror("Error", "Please select an audio file")
            return
        if not model:
            messagebox.showerror("Error", "Please select a model")
            return

        messagebox.showinfo("Good", "Running docker container")
        subprocess.run(
            ["docker-compose", "run", "whisper", "python", "main.py"], check=False
        )
        messagebox.showinfo("Finished", "Docker container finished running")

    def stop(self):
        subprocess.run(["docker-compose", "down"], check=False)
        messagebox.showinfo("Stopped", "Docker container stopped")


if __name__ == "__main__":
    os.makedirs(USER_AUDIO_DIR, exist_ok=True)
    os.makedirs(USER_OUTPUT_DIR, exist_ok=True)
    app = WhisperGUI()
    app.mainloop()
