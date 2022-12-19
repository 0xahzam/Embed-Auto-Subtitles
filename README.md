# Embed Auto Subtitles

This program uses `ffmpeg` and [Open AI's Whisper](https://openai.com/blog/whisper) to transcribe audio from video in English and then render the subtitles and return an output video.

## Prerequisite
You'll need to install [`ffmpeg`](https://ffmpeg.org/)
```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg
```
You'll also need to setup [Open AI's Whisper](https://github.com/openai/whisper)
```
pip install git+https://github.com/openai/whisper.git 
```