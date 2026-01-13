import os

from pathlib import Path
from pydub import AudioSegment
from pytubefix import YouTube
from pytubefix.cli import on_progress

VIDEO_FOLDER = "temp_videos"
AUDIO_FOLDER = "audios"
url = input("Enter URL: ")

yt = YouTube(url, on_progress_callback=on_progress)
title = yt.title

# Get video
ys = yt.streams.get_highest_resolution()
file_name = f"{title}.mp4"
video_path = f"{VIDEO_FOLDER}/"

# Download video
ys.download(output_path=video_path)

# Save audio
current_dir = Path(__file__).resolve().parent
print(f"Current directory: {current_dir}")
full_video_path = (
    f"{current_dir.parent}/youtube-audio-downloader/{video_path}/{file_name}"
)
audio = AudioSegment.from_file(full_video_path, format="mp4")
audio.export(f"{AUDIO_FOLDER}/{title}_audio.mp3", format="mp3")
print(f"Successfully downloaded audio of {title}")

# Delete video
os.remove(full_video_path)
