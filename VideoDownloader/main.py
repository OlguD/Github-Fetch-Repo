import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import os
from pytube import Playlist
import re
import threading

# root window
root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title('YouTube Video Downloader')

SAVE_PATH = os.path.expanduser("~/Desktop/Video")

# store email address and password
link = tk.StringVar()

def login_clicked():
    global video
    """ callback when the login button clicked
    """
    #yt = YouTube(link.get(), on_progress_callback=on_progress)
    #video = yt.streams.get_highest_resolution()
    #video.download(SAVE_PATH)
    playlist = Playlist(link.get())
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    print(f"Playlist length: {len(playlist.video_urls)}")
    # physically downloading the audio track
    for video in playlist.videos:
        audioStream = video.streams.get_by_itag("140")
        audioStream.download(output_path=SAVE_PATH)

# Sign in frame
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(frame, text="Video Link")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(frame, textvariable=link)
email_entry.pack(fill='x', expand=True)

loadingPercent = tk.Label(frame, text="0", fg="white", font=("Agency FB", 30))
loadingPercent.pack(fill="x")

# indeterminate progress bar
progressbar = ttk.Progressbar(frame, orient="horizontal", length=500, mode='indeterminate')
progressbar.pack(fill='x')
progressbar.start()

# login button
download_button = ttk.Button(frame, text="Download", command=login_clicked)
download_button.pack(fill='x', expand=True, pady=10)


root.mainloop()