import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

# directory_path = os.path.dirname(__file__)

class App:
    ''' Currently just a shell, this gui will take inputs '''
    # Creates a Gui window
    def __init__(self, window):
        self.window = window
        self.window.title("Scrumdog Gui")
        self.window.geometry("520x250")
        self.window.resizable(False, False)

        # Create and resize background photo
        # original_img = Image.open(os.path.join(directory_path, "Photo.png"))
        # resized_image = original_img.resize((520, 180))
        # self.new_image = ImageTk.PhotoImage(resized_image)
        # self.background_label = tk.Label(window, image=self.new_image)
        # self.background_label.place(relwidth=1, relheight=1)

        # Frame for the entry boxes
        entry_frame = tk.Frame(window)
        entry_frame.pack(pady=10)

        # Number of students entry box
        tk.Label(entry_frame, text="Number of Students:").grid(row=0, column=0, padx=5)
        self.keyword1_entry = tk.Entry(entry_frame, width=15)
        self.keyword1_entry.grid(row=0, column=1, padx=5)

        # Number of signs to display entry box
        tk.Label(entry_frame, text="Number of Signs to Display:").grid(row=0, column=2, padx=5)
        self.keyword2_entry = tk.Entry(entry_frame, width=15)
        self.keyword2_entry.grid(row=0, column=3, padx=5)

        # Sign display time entry box
        tk.Label(entry_frame, text="Time of Sign Display(seconds):").grid(row=1, column=0, padx=5)
        self.keyword3_entry = tk.Entry(entry_frame, width=15)
        self.keyword3_entry.grid(row=1, column=1, padx=5)

        # Time std dev entry box
        tk.Label(entry_frame, text="Variation in Display Time(seconds):").grid(row=1, column=2, padx=5)
        self.keyword4_entry = tk.Entry(entry_frame, width=15)
        self.keyword4_entry.grid(row=1, column=3, padx=5)

        # Speed of cars entry box
        tk.Label(entry_frame, text="Speed of Cars(mph):").grid(row=2, column=0, padx=5)
        self.keyword5_entry = tk.Entry(entry_frame, width=15)
        self.keyword5_entry.grid(row=2, column=1, padx=5)

        # Variation of car speed keyword entry box
        tk.Label(entry_frame, text="Car Speed Variation(mph):").grid(row=2, column=2, padx=5)
        self.keyword6_entry = tk.Entry(entry_frame, width=15)
        self.keyword6_entry.grid(row=2, column=3, padx=5)

        # Display Results
        self.results = tk.Text(window, height=7, width=60)
        self.results.pack(padx=5, pady=5)

        # # Result label
        # self.result_label = tk.Label(window, text="Results")
        # self.result_label.pack(pady=10)

        # Submit button
        self.submit_button = tk.Button(window, text="Submit", width=20)
        self.submit_button.pack(pady=10)

if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()
