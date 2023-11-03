import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.playlist = []
        self.current_track = 0

        pygame.init()

        self.create_widgets()
    
    def create_widgets(self):
        # Create the playlist frame
        playlist_frame = tk.Frame(self.root)
        playlist_frame.pack(pady=10)

        # Create the buttons frame
        button_frame = tk.Frame(self.root)
        button_frame.pack()
 
        # Create the playlist label
        self.playlist_label = tk.Label(playlist_frame, text="Playlist")
        self.playlist_label.pack()

        # Create the playlist listbox
        self.playlist_listbox = tk.Listbox(playlist_frame, selectmode=tk.SINGLE, selectbackground="black")
        self.playlist_listbox.pack(fill=tk.BOTH, expand=1)

        # Create the buttons
        play_button = tk.Button(button_frame, text="Play", command=self.play_music)
        pause_button = tk.Button(button_frame, text="Pause", command=self.pause_music)
        stop_button = tk.Button(button_frame, text="Stop", command=self.stop_music)
        next_button = tk.Button(button_frame, text="Next", command=self.next_music)
        prev_button = tk.Button(button_frame, text="Previous", command=self.prev_music)
        add_button = tk.Button(button_frame, text="Add Song", command=self.add_song)

        play_button.grid(row=0, column=0, padx=10)
        pause_button.grid(row=0, column=1, padx=10)
        stop_button.grid(row=0, column=2, padx=10)
        prev_button.grid(row=0, column=3, padx=10)
        next_button.grid(row=0, column=4, padx=10)
        add_button.grid(row=0, column=5, padx=10)

    def add_song(self):
        song = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if song:
            self.playlist.append(song)
            self.playlist_listbox.insert(tk.END, os.path.basename(song))

    def play_music(self):
        if pygame.mixer.music.get_busy() == 0 and len(self.playlist) > 0:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()
    
    def pause_music(self):
        pygame.mixer.music.pause()
    
    def stop_music(self):
        pygame.mixer.music.stop()
    
    def next_music(self):
        if self.current_track < len(self.playlist) - 1:
            self.current_track += 1
        else:
            self.current_track = 0
        self.play_music()
    
    def prev_music(self):
        if self.current_track > 0:
            self.current_track -= 1
        else:
            self.current_track = len(self.playlist) - 1
        self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
