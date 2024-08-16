import cv2
import numpy as np
import time

# Paths to your video files
video1 = "C:\\Users\\burke\\OneDrive\\Desktop\\NeuroIOT\\RW1\\GH010069.mp4"
video2 = "C:\\Users\\burke\\OneDrive\\Desktop\\NeuroIOT\\Output Video Example\\output_video.mp4"

# Load the two videos
cap1 = cv2.VideoCapture(video1)
cap2 = cv2.VideoCapture(video2)

# Check if videos are loaded successfully
if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open one of the videos.")
    exit()

# Get properties of the videos
width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))

width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))

# Define the maximum dimensions for the display window
max_height = 540  # Set your desired maximum height
max_width = 960   # Set your desired maximum width

# Resize the videos to match dimensions (optional)
height = min(height1, height2, max_height)
width = min(width1, width2, max_width)

# GoPro video offset for synchronization
GoproOffsetForSync = 60.57  # Start the GoPro video

# Timer offset in seconds
OffsetForTimer = GoproOffsetForSync  # Start the timer at the GoPro offset

# Apply the GoPro offset by setting the position in the video
cap1.set(cv2.CAP_PROP_POS_MSEC, GoproOffsetForSync * 1000)

paused = False
start_time = OffsetForTimer  # Initialize the start time with the offset
start_time_second_video = 0  # Initialize the second video's start time independently
pause_time = 0  # Time when paused
last_time = time.time()

# Timers for controlling frame rate
last_time1 = time.time()
last_time2 = time.time()

# Initialize the frames after applying the GoPro offset
ret1, frame1 = cap1.read()
ret2, frame2 = cap2.read()

# Define text to display
instructions = [
    "Press 'q' to quit.",
    "Press 'p' to pause/resume.",
    "Press 'a' to go back 0.5 seconds.",
    "Press 'd' to go forward 0.5 seconds."
]

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5  # Smaller font size for instructions
font_color = (255, 255, 255)
font_thickness = 1  # Thinner text for instructions
line_type = cv2.LINE_AA

# Calculate space needed for text with extra padding
text_height = int(height * 0.2)  # Adjusted height for the text box

def show_frame(elapsed_time):
    # Resize frames to ensure they are the same size
    frame1_resized = cv2.resize(frame1, (width, height))
    frame2_resized = cv2.resize(frame2, (width, height))

    # Concatenate frames horizontally (side by side)
    combined_frame = np.hstack((frame1_resized, frame2_resized))

    # Create a black background for the text
    text_background = np.zeros((text_height, combined_frame.shape[1], 3), dtype=np.uint8)

    # Overlay the instructions on the black background with more padding
    y0, dy = 20, 25  # Adjusted vertical position and line spacing
    for i, line in enumerate(instructions):
        y = y0 + i * dy
        cv2.putText(text_background, line, (10, y), font, font_scale, font_color, font_thickness, line_type)

    # Stack the text background on top of the combined video frame
    combined_frame_with_text = np.vstack((text_background, combined_frame))

    # Calculate minutes, seconds, and hundredths of a second
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    hundredths = int((elapsed_time * 100) % 100)

    # Display the timestamp at the bottom
    elapsed_time_str = f"{minutes:02}:{seconds:02}.{hundredths:02}"
    cv2.putText(combined_frame_with_text, f"Timestamp: {elapsed_time_str}",
                (10, combined_frame_with_text.shape[0] - 10),
                font, font_scale, font_color, font_thickness, line_type)

    # Display the resulting frame
    cv2.imshow('Videos Playing Side by Side', combined_frame_with_text)

while True:
    if not paused:
        current_time = time.time()

        # Calculate elapsed time for the timer display
        start_time += (current_time - last_time)
        last_time = current_time

        # Calculate the position for the second video relative to the GoPro video
        start_time_second_video = start_time - OffsetForTimer

        # Read and update frame from the first video (GoPro) according to its frame rate
        if (current_time - last_time1) >= (1 / fps1):
            ret1, frame1 = cap1.read()
            last_time1 = current_time

        # Read and update frame from the second video according to its frame rate
        if (current_time - last_time2) >= (1 / fps2):
            ret2, frame2 = cap2.read()
            last_time2 = current_time

        if not ret1 or not ret2:
            break

        show_frame(start_time)

    key = cv2.waitKey(1) & 0xFF  # Use waitKey(1) for real-time key checking

    # Press 'q' on the keyboard to exit the loop
    if key == ord('q'):
        break
    # Press 'p' to pause and resume
    elif key == ord('p'):
        if paused:
            # Resuming from pause
            last_time = time.time()
        else:
            # Pausing the video
            pause_time = time.time()
            start_time += (pause_time - last_time)

        paused = not paused
    # Press 'a' to go back 0.5 seconds
    elif key == ord('a'):  # 'a' represents the left arrow key
        # Move back by 0.5 seconds
        new_time = max(OffsetForTimer, start_time - 0.5)

        # Calculate the new position for both videos
        new_time_gopro = new_time
        new_time_second_video = new_time - OffsetForTimer

        # Set the new position in the GoPro video
        cap1.set(cv2.CAP_PROP_POS_MSEC, new_time_gopro * 1000)

        # Set the new position in the second video
        cap2.set(cv2.CAP_PROP_POS_MSEC, new_time_second_video * 1000)

        # Read the new frames
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        # Update the start times
        start_time = new_time
        start_time_second_video = new_time_second_video

        # Show the frame after moving back
        show_frame(start_time)

        paused = True  # Keep the video paused after moving back
    # Press 'd' to go forward 0.5 seconds
    elif key == ord('d'):  # 'd' represents the right arrow key
        # Move forward by 0.5 seconds
        new_time = start_time + 0.5

        # Calculate the new position for both videos
        new_time_gopro = new_time
        new_time_second_video = new_time - OffsetForTimer

        # Set the new position in the GoPro video
        cap1.set(cv2.CAP_PROP_POS_MSEC, new_time_gopro * 1000)

        # Set the new position in the second video
        cap2.set(cv2.CAP_PROP_POS_MSEC, new_time_second_video * 1000)

        # Read the new frames
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        # Update the start times
        start_time = new_time
        start_time_second_video = new_time_second_video

        # Show the frame after moving forward
        show_frame(start_time)

        paused = True  # Keep the video paused after moving forward

# Release the video captures and close the display window
cap1.release()
cap2.release()
cv2.destroyAllWindows()