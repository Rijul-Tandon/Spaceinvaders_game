from PIL import Image

# Load the image using a raw string
image = Image.open(r'C:\Users\letsc\OneDrive\Desktop\pygame\spaceenvaders\player.png')

# Get dimensions
width, height = image.size
print(f"Width: {width} pixels")
print(f"Height: {height} pixels")
