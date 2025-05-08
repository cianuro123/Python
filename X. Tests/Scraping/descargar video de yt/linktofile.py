from pytube import YouTube
import pytube
from os import system
if system!=0:system("cls")


def download_video(video_url,filename):
    try:
        print(f"Processing URL:{video_url}")
        yt= YouTube(video_url)
        print(f"Video creado {yt}")
        print("Available streams: ")
        if not yt.streams:
            print("no streams available")
            return
        stream= yt.streams.get_highest_resolution()
        stream.download(filename)
        print("Download complete")
    except ValueError:
        print("Invalid URL. Please check the link.")
        
    except Exception as e:
        print("An error occurred:", e)
        
def download_audio(video_url, output_path,filename):
    try:
        
        yt_audio = pytube.YouTube(video_url)
        yt_audio.streams.filter(only_audio=True).first().download(output_path, filename)
        
    except ValueError:
        print("Invalid URL. Please check the link.")
        
    except pytube.exceptions.VideoUnavailable:
        print("Video is unavailable. Please check the link.")
        
download_video("https://www.youtube.com/watch?v=NPbWhDaESds","test.mp4")
# download_audio("https://www.youtube.com/watch?v=NPbWhDaESds","test.mp3")