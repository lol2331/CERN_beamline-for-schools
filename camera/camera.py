import picamera

# Initialize the camera
camera = picamera.PiCamera()

# Set the resolution of the camera
camera.resolution = (1024, 768)

# Set the number of photos you want to take
num_photos = 5

# Loop through and take the photos
for i in range(num_photos):
    # Take a photo and save it to the specified folder
    filename = f'image{i}.jpg'
    camera.capture(f'"C:\Users\Andrei\OneDrive\Documente\photos"{filename}')
