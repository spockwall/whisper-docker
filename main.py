import whisper

MODEL_ROOT = "/app/models"
AUDIO_ROOT = "/app/audios"
AUDIO_FILE = "test.mp3"


model = whisper.load_model("small", download_root=MODEL_ROOT)

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio(AUDIO_ROOT + "/" + AUDIO_FILE)
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
