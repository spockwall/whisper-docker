# Openai-whisper

## Description
Running openai-whisper in docker container


## How to use 
1. Enter directory: "/whisper"
2. Put the audio files in /audios, file types can be mp3, mp4, wav
3. change the audio file names in main.py
4. Run the following commands
    ```shellscript=
    $ cd whisper
    $ docker-compose build
    $ docker-compose run whisper python main.py
    ```
5. Waiting ....
6. check the output files in "/outputs"

## Notice
1. Do not modify "/models", "docker-compose.yml", and "Dockerfile" 
2. Do not change the relative positions of the files and folders.