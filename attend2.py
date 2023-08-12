from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import Image, ImageTk
import csv
import os

# Path to the attendance folder
path = "D:\Mayur\code\Online-Face-Attendance--master\Attendance"

# Load known images
images = []
classnames = []
mylist = os.listdir(path)
for cl in mylist:
    cur_img = cv2.imread(f'{path}/{cl}')
    images.append(cur_img)
    classnames.append(os.path.splitext(cl)[0])

# Face encoding function
def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

session_id = datetime.now().strftime("%Y-%m-%d_%H-%M")
marked_names = set()

def markattendance(name):
    if name in marked_names:
        messagebox.showinfo("Attendance", f"{name} has already been marked present in this session!")
        return
    
    now = datetime.now()
    datestring = now.strftime("%d/%m/%Y")
    timestring = now.strftime("%H:%M:%S")
    
    filename = f"attendance_{session_id}.csv"
    directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    file_path = os.path.join(directory, filename)  # Create the file path
    
    # Check if the file already exists
    file_exists = os.path.exists(file_path)
    
    with open(file_path, "a", newline='') as f:
        writer = csv.writer(f)
        
        # Write column headers only if the file doesn't exist
        if not file_exists:
            writer.writerow(["Name", "Date", "Time"])
        
        writer.writerow([name, datestring, timestring])  # Write attendance data
        messagebox.showinfo("Attendance", f"{name} is marked present!")
        
    # Add the name to the set of marked names
    marked_names.add(name)
                 

# Face recognition and GUI
encodelistknown = findEncodings(images)

# Create Tkinter window
window = Tk()
window.title("Face Attendance System")

# Create a canvas for displaying the video feed
canvas = Canvas(window, width=640, height=480)
canvas.pack()

# Start video capture
cap = cv2.VideoCapture(0)



def process_frame():
    success, img = cap.read()
    if success:
        imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
        facecurframe = face_recognition.face_locations(imgs)
        encodecurframe = face_recognition.face_encodings(imgs, facecurframe)

        for encodeface, faceloc in zip(encodecurframe, facecurframe):
            matches = face_recognition.compare_faces(encodelistknown, encodeface)
            facedist = face_recognition.face_distance(encodelistknown, encodeface)
            matchindex = np.argmin(facedist)

            if matches[matchindex]:
                name = classnames[matchindex].upper()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markattendance(name)
        

        # Convert the image array to PIL Image
        img = Image.fromarray(img)

        # Update the canvas with the new image
        canvas.img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=NW, image=canvas.img)

    # Call the process_frame function after 1ms (update rate = 1000ms / 1ms = 1fps)
    window.after(1, process_frame)


# Start processing frames
process_frame()



# Run the Tkinter event loop
window.mainloop()
