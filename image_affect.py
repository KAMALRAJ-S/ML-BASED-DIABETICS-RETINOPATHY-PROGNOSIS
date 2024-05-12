from PIL import Image

# Load the image from file
image = Image.open('capture.jpg')

# Convert the image to grayscale
image = image.convert('L')

# Define a threshold value
threshold = 100

# Calculate the number of affected pixels
affected_pixels = 0
total_pixels = image.width * image.height

for x in range(image.width):
    for y in range(image.height):
        if image.getpixel((x, y)) < threshold:
            affected_pixels += 1

# Calculate the affected percentage
affected_percentage = (affected_pixels / total_pixels) * 100

# Print the result
print(f'Affected percentage: {affected_percentage}%')
