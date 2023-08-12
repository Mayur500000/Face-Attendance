#import face_recognition
#import cv2
import numpy as np
import csv
from datetime import datetime
import tkinter as tk

#video_capture = cv2.VideoCapture(0)

# Rest of the code...

# Create the GUI window
window = tk.Tk()
window.title("Face Recognition Attendance System")

# Create a label for displaying recognized names
name_label = tk.Label(window, text="", font=("Helvetica", 16))
name_label.pack()

def update_name_label(name):
    name_label.config(text=name)

# Rest of the GUI components and event handlers...

# Update the GUI with recognized names
#for face_name in face_names:
    #update_name_label(face_name)

# Rest of the code...

# Start the GUI main loop
window.mainloop()

# Rest of the code...