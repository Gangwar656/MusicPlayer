import tkinter as tk
from tkinter import filedialog
import os
import pygame
import random
from PIL import Image, ImageTk

class MusicPlayer:
    def __init__(self, root):  # Corrected __init__
        self.root = root
        self.root.title("Music Player for PY PRoj")
        self.root.geometry("1200x800")
        self.root.config(bg='black')

        # Load background image
        self.bg_image = Image.open(r"C:\Users\Reena devi\Desktop\ai-generated-studio-shot-of-black-headphones-over-music-note-explosion-background-with-empty-space-for-text-photo.jpg")
        self.bg_image = self.bg_image.resize((1200, 800), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a Label to hold the background image
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        pygame.mixer.init()
        self.music_files = []
        self.current_track = -1
        self.shuffle_mode = False

        # Create Listbox for displaying songs
        self.listbox = tk.Listbox(self.root, bg='black', fg='white', width=100, height=20, font=('Helvetica', 12))
        self.listbox.pack(pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.on_song_select)

        self.current_song_label = tk.Label(self.root, text="No song playing", bg='black', fg='cyan', font=('Helvetica', 14))
        self.current_song_label.pack(pady=10)

        button_style = {'bg': 'cyan', 'font': ('Helvetica', 10, 'bold')}
        
        self.load_button = tk.Button(self.root, text="Load Album", command=self.load_album, **button_style)
        self.load_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music, **button_style)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music, **button_style)
        self.stop_button.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_track, **button_style)
        self.next_button.pack(pady=5)

        self.previous_button = tk.Button(self.root, text="Previous", command=self.previous_track, **button_style)
        self.previous_button.pack(pady=5)

        self.shuffle_button = tk.Button(self.root, text="Shuffle", command=self.toggle_shuffle, **button_style)
        self.shuffle_button.pack(pady=5)

        # Volume Control
        self.volume_label = tk.Label(self.root, text="Volume", bg='black', fg='cyan', font=('Helvetica', 12))
        self.volume_label.pack(pady=5)
        
        self.volume_scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume, bg='black', fg='cyan', font=('Helvetica', 10))
        self.volume_scale.set(50)
        self.volume_scale.pack(pady=5)

        # Playback Progress Bar
        self.progress_scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, bg='black', fg='cyan', font=('Helvetica', 10), length=800, showvalue=0)
        self.progress_scale.pack(pady=5)

        self.update_progress()

    def load_album(self):
        folder = filedialog.askdirectory()
        if folder:
            self.music_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.mp3')]
            if self.music_files:
                self.current_track = 0
                self.listbox.delete(0, tk.END) 
                for file in self.music_files:
                    self.listbox.insert(tk.END, os.path.basename(file)) 
                print(f"Loaded: {[os.path.basename(f) for f in self.music_files]}")

    def play_music(self):
        if self.music_files and self.current_track >= 0:
            pygame.mixer.music.load(self.music_files[self.current_track])
            pygame.mixer.music.play()
            self.current_song_label.config(text=f"Now Playing: {os.path.basename(self.music_files[self.current_track])}")
            self.update_progress()

    def on_song_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            self.current_track = selection[0] 
            self.play_music()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_song_label.config(text="No song playing")

    def next_track(self):
        if self.music_files:
            if self.shuffle_mode:
                self.current_track = random.randint(0, len(self.music_files) - 1)
            else:
                self.current_track = (self.current_track + 1) % len(self.music_files)
            self.play_music()

    def previous_track(self):
        if self.music_files:
            self.current_track = (self.current_track - 1) % len(self.music_files)
            self.play_music()

    def toggle_shuffle(self):
        self.shuffle_mode = not self.shuffle_mode
        if self.shuffle_mode:
            self.shuffle_button.config(bg="lightgreen")  
            print("Shuffle Mode: ON")
        else:
            self.shuffle_button.config(bg="darkblue") 
            print("Shuffle Mode: OFF")

    def set_volume(self, volume):
        volume = int(volume) / 100
        pygame.mixer.music.set_volume(volume)

    def update_progress(self):
        if self.music_files and self.current_track >= 0:
            current_time = pygame.mixer.music.get_pos() / 1000  # Convert to seconds
            if pygame.mixer.music.get_busy():
                total_length = self.get_song_length(self.music_files[self.current_track])
                progress_percentage = (current_time / total_length) * 100
                self.progress_scale.set(progress_percentage)
                self.root.after(1000, self.update_progress)  # Update every second

    def get_song_length(self, filepath):
        # Placeholder: You should implement actual length retrieval here
        return 180  # Assume each song is 3 minutes

class HomePage:
    def __init__(self, master):  # Corrected __init__
        self.master = master
        self.master.title("Home Page")
        self.master.geometry("1200x800")
        self.master.config(bg='black')

        self.bg_image = Image.open(r"C:\Users\Reena devi\Desktop\ai-generated-studio-shot-of-black-headphones-over-music-note-explosion-background-with-empty-space-for-text-photo.jpg")
        self.bg_image = self.bg_image.resize((1200, 800), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.title_label = tk.Label(self.master, text="Welcome to the Music Hub", bg='black', fg='cyan', font=('Helvetica', 24))
        self.title_label.pack(pady=20)

        self.enter_button = tk.Button(self.master, text="Enter Music Hub", command=self.enter_music_hub, bg='cyan', font=('Helvetica', 14, 'bold'))
        self.enter_button.pack(pady=20)

    def enter_music_hub(self):
        self.master.destroy()  
        self.open_music_player()  

    def open_music_player(self):
        root = tk.Tk()
        music_player = MusicPlayer(root)
        root.mainloop()

if __name__ == "__main__":  # Corrected __main__
    home_root = tk.Tk()
    home_page = HomePage(home_root)
    home_root.mainloop()
