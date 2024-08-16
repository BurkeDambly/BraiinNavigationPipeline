import cv2
import os

# if cv2 throws error run this line in command prompt
#pip install opencv-python

def images_to_video(image_folder, output_folder, video_name, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    images.sort()  # Sort images if needed

    if not images:
        print("No images found in the folder.")
        return

    # Read the first image to get dimensions
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'XVID', 'MJPG', etc.
    video_path = os.path.join(output_folder, video_name)
    video = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

    for image in images:
        frame = cv2.imread(os.path.join(image_folder, image))
        video.write(frame)

    video.release()
    print(f"Video saved at {video_path}")


# Usage
image_folder = 'C:\\Users\\burke\\OneDrive\\Desktop\\NeuroIOT\\FiguresExample'
output_folder = 'C:\\Users\\burke\\OneDrive\\Desktop\\NeuroIOT\\Output Video Example'
video_name = 'output_video.mp4'
fps = 2  # Frames per second

images_to_video(image_folder, output_folder, video_name, fps)