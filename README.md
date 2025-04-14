# Openai-whisper

## Description
Running openai-whisper in docker container


## How to use 
1. Enter directory: "/whisper"
2. If you want to disable internet, set "internal" true in "docker-compose.yml", otherwise set false
3. Put the audio files in /audios, file types can be mp3, mp4, wav
4. change the audio file names in main.py
5. Run the following commands
    ```shellscript=
    $ cd whisper
    $ docker-compose build 
    $ docker-compose run whisper python main.py
    ```
6. Waiting ....
7. check the output files in "/outputs"

## Notice
1. Do not modify "/models"
2. Do not change the relative positions of the files and folders.