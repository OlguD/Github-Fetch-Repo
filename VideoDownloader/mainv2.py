from pytube import YouTube
import tkinter as tk
from tkinter import ttk
import threading
import os
import re
from pytube import Playlist

# main application shows:
# label Loading..
# label which configure values when file is downloading 
# inderterminate progress bar
class MainApplication(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master)
        self.link = tk.StringVar()
        self.master = master
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_columnconfigure(0, weight=1)

        self.youtubeEntry = ttk.Entry(self.master, textvariable=self.link)
        self.youtubeEntry.grid(pady=(150, 0))
        self.FolderLoacation = os.path.expanduser("~/Desktop/Video")

        # pytube
        self.yt = Playlist(self.youtubeEntry)
        self.yt._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

        for video in self.yt.videos:
            self.DownloadFile(video,self.FolderLoacation)


        video_type = self.yt.streams.filter(res="720p",mime_type="video/mp4").first()

        # file size of a file
        self.MaxfileSize = video_type.filesize
        # Loading label
        self.loadingLabel = ttk.Label(self.master, text="Loading...", font=("Agency FB", 30))
        self.loadingLabel.grid(pady=(100,0))

        # loading precent label which must show % donwloaded
        self.loadingPercent = tk.Label(self.master, text="0", fg="green", font=("Agency FB", 30))
        self.loadingPercent.grid(pady=(30,30))

        # indeterminate progress bar
        self.progressbar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode='indeterminate')
        self.progressbar.grid(pady=(50,0))
        self.progressbar.start()    

        threading.Thread(target=self.yt.register_on_progress_callback(self.show_progress_bar)).start()

        # call Download file func
        threading.Thread(target=self.DownloadFile).start()



    def DownloadFile(self,video,folder):
        self.video.streams.filter(res="720p",mime_type="video/mp4").first().download(folder)

    # func count precent of a file
    def show_progress_bar(self, stream=None, chunk=None, file_handle=None, bytes_remaining=None):

        # loadingPercent label configure value %
        self.loadingPercent.config(text=str(int(100 - (100*(bytes_remaining/self.MaxfileSize)))))

if __name__ == "__main__":
    root = tk.Tk() 
    root.title('YouTube Video Downloader')
    root.geometry("600x400")
    root.resizable(False, False)
    app = MainApplication(root)
    root.mainloop()