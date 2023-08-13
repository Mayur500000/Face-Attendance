import cv2
import os
import sys

def capture_photo(name):
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Unable to open the camera.")
        return

    # Flag to indicate if the camera window is open
    window_open = True

    # Read and display frames from the camera
    while window_open:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)

        # Wait for the 's' key to capture a photo
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Specify the path to the folder where you want to save the photo
            folder_path = r'D:\\Mayur\\code\\Online-Face-Attendance--master\Attendance'

            # Check if the folder exists, create it if necessary
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Save the photo with the provided name
            photo_path = os.path.join(folder_path, f'{name}.jpg')
            cv2.imwrite(photo_path, frame)
            print(f"Photo captured and saved as {name}.jpg.")
            break

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            window_open = False

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

# Check if the name is provided as an argument
if len(sys.argv) > 1:
    name = sys.argv[1]
    capture_photo(name)
else:
    print("No name provided.")
