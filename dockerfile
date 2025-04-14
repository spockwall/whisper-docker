FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg git && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -U openai-whisper
RUN pip install setuptools-rust

WORKDIR /app

CMD ["bash"]