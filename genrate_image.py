from PIL import Image, ImageDraw, ImageFont
import os

# Make sure static folder exists
os.makedirs("static", exist_ok=True)

# Create image
img = Image.new('RGB', (400, 250), color=(173, 216, 230))  # light blue
draw = ImageDraw.Draw(img)

text = "✅ Deployment Successful!"
font_size = 24

# Load default font
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except:
    font = ImageFont.load_default()

# Calculate text width and height
bbox = draw.textbbox((0, 0), text, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]

# Center text
x = (400 - w) / 2
y = (250 - h) / 2
draw.text((x, y), text, fill=(0, 100, 0), font=font)

# Save the image in static folder
img.save("static/success.png")
print("✅ success.png created in static/")

