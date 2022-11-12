import re
from pytube import Playlist
import os

DOWNLOAD_DIR = os.path.expanduser("~/Desktop/Video")

PlayList_url = str(input("Playlist link: "))

playlist = Playlist(PlayList_url)

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))


for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(DOWNLOAD_DIR)