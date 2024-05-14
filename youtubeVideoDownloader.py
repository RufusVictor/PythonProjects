import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download()
        messagebox.showinfo("Success", f"Video downloaded successfully!\nFile saved at: {file_path}")
    except RegexMatchError:
        messagebox.showerror("Error", "Invalid URL format")
    except VideoUnavailable:
        messagebox.showerror("Error", "The video is unavailable")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x200")
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)
download_button = tk.Button(root, text="Download Video", command=download_video, fg="white", bg="green", font=("Arial", 12))
download_button.pack(pady=20)
root.mainloop()