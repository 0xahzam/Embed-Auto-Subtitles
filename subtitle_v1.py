import subprocess

filename = input("Enter name of the file :\n")

srt = 'whisper {} --model tiny --task translate'.format(filename)
srtlist = srt.split()
output = 'ffmpeg -i {} -vf subtitles={}.srt output.mp4'.format(filename,filename)
outputlist = output.split()

def transcribe(file):
        subprocess.call(srtlist)

transcribed = transcribe(filename)
subprocess.call(outputlist)

