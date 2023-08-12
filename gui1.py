import os
from tkinter import *
from tkinter import messagebox
import subprocess

# Define the command to run the attend2.py script
attend_script = "C:\\Users\\91970\\Downloads\\Updated Attendence\\Online-Face-Attendance--master\\Online-Face-Attendance--master\\attend2.py"

# Define the command to run the final.py script
final_script = "C:\\Users\\91970\\Downloads\\Updated Attendence\\Online-Face-Attendance--master\\Online-Face-Attendance--master\\final.py"

Cview_script = "C:\\Users\\91970\\Downloads\\Updated Attendence\\Online-Face-Attendance--master\\Online-Face-Attendance--master\\Cview.py"

out_script = "C:\\Users\\91970\\Downloads\\Updated Attendence\\Online-Face-Attendance--master\\Online-Face-Attendance--master\\out.py"

new_pic_script = "C:\\Users\\91970\\Downloads\\Updated Attendence\\Online-Face-Attendance--master\\Online-Face-Attendance--master\\new_pic.py"

# Function to execute the attend2.py script
def run_attend_script():
    try:
        subprocess.run(["python", attend_script])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run attend2.py script:\n{str(e)}")

# Function to execute the out.py script
def run_out_script():
    try:
        subprocess.run(["python", out_script])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run out.py script:\n{str(e)}")

# Function to execute the final.py script
def run_final_script():
    try:
        subprocess.run(["python", final_script])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run final.py script:\n{str(e)}")

# Function to execute the Cview.py script
def run_Cview_script():
    try:
        subprocess.run(["python", Cview_script])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Cview.py script:\n{str(e)}")

# Function to execute the new_pic.py script
def run_new_pic_script():
    # Create a new Tkinter window
    name_window = Tk()
    name_window.title("Enter Name")
    name_window.geometry("300x100")
    
    # Create an Entry widget to input the name
    name_entry = Entry(name_window, width=30)
    name_entry.pack(pady=10)
    # Function to capture the name and run new_pic.py
    def capture_name():
        name = name_entry.get()
        name_window.destroy()
        if name:
            messagebox.showinfo("Info", "Press 's' to take a photo.")
            try:
                subprocess.run(["python", new_pic_script, name])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to run new_pic.py script:\n{str(e)}")
        else:
            messagebox.showinfo("Info", "No name entered.")

    # Create a button to submit the name
    submit_button = Button(name_window, text="Submit", command=capture_name)
    submit_button.pack()
    
    

    # Run the name_window event loop
    name_window.mainloop()

# Create Tkinter window
window = Tk()
window.title("Attendance Processing")
window.geometry("420x420")

# Create buttons
button1 = Button(window, text="Take Attendance", command=run_attend_script)
button1.pack(pady=10)

button2 = Button(window, text="Process Data", command=run_final_script)
button2.pack(pady=10)

button3 = Button(window, text="View Final Attendance", command=run_Cview_script)
button3.pack(pady=10)

button4 = Button(window, text="Mark Exit", command=run_out_script)
button4.pack(pady=10)

button5 = Button(window, text="New Entry", command=run_new_pic_script)
button5.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
