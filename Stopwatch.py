import tkinter as tk
import time
from customtkinter import *

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("250x150")
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.label = CTkLabel(root, text="00:00:00", font=("Arial", 60))
        self.label.pack(pady=20)

        self.start_button = CTkButton(root, text="Start", font=("Arial", 20), command=self.start, width=20)
        self.start_button.place(relx = 0.05, rely = 0.7)

        self.stop_button = CTkButton(root, text="Stop", command=self.stop , width=20, font=("Arial", 20),)
        self.stop_button.place(relx = 0.38, rely = 0.7)

        self.reset_button = CTkButton(root, text="Reset", command=self.reset, width=20, font=("Arial", 20),)
        self.reset_button.place(relx = 0.695, rely = 0.7)

    def update_time(self):
        if self.running:
            current_time = time.time()
            self.elapsed_time = current_time - self.start_time
            formatted_time = self.format_time(self.elapsed_time)
            self.label.configure(text=formatted_time)
            self.root.after(100, self.update_time)

    def format_time(self, elapsed_time):
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 100)
        return f"{minutes:02}:{seconds:02}:{milliseconds:02}"

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.label.configure(text="00:00:00")


if __name__ == "__main__":
    root = CTk()
    app = Stopwatch(root)
    root.mainloop()
