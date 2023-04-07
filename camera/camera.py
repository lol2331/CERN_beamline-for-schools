import os
from PIL import Image
import picamera
import time

# Set the folder to save the photos
folder_path = "C:\Users\Andrei\OneDrive\Documente\camera\photos"

def check_dead_pixels(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the width and height of the image
    width, height = image.size

    # Loop through all pixels in the image
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = image.getpixel((x, y))

            # Check if the pixel is black (dead)
            if r == g == b == 0:
                print(f"Dead pixel found at ({x}, {y})")

# Initialize the camera
camera = picamera.PiCamera()

# Set the resolution of the camera
camera.resolution = (1024, 768)

# Set the number of photos you want to take
num_photos = 20

# Loop through and take the photos
for i in range(num_photos):
    # Take a photo and save it to the specified folder
    filename = f"image{i}.jpg"
    image_path = os.path.join(folder_path, filename)
    camera.capture(image_path)

    # Check for dead pixels in the photo
    check_dead_pixels(image_path)

    time.sleep(60)
