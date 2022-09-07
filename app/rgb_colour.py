# Get the rgb values for each frame as a list of tuples?
from email.mime import image
import os
from PIL import Image

frame_directory = r'video_frames/0.png'
image_file = Image.open(frame_directory)
dominant_colour = sorted(image_file.getcolors(2**24), reverse=True)[0][1]
print(dominant_colour)