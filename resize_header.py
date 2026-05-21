from PIL import Image
import os

# Open original image
img = Image.open('Projects/header-image.png')
print(f'Original: {img.width}x{img.height}px')

# Resize to optimal dimensions
# Height: 20em = 320px
# Width: to fit content area, resize to 960px wide (maintains aspect ratio)
target_width = 960
target_height = int(960 / (img.width / img.height))

resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
print(f'Resized to: {resized.width}x{resized.height}px')

# Save back to the same location
resized.save('Projects/header-image.png', quality=95, optimize=True)
print(f'Saved to Projects/header-image.png')

# Show file size
file_size_mb = os.path.getsize('Projects/header-image.png') / (1024 * 1024)
print(f'New file size: {file_size_mb:.2f}MB')
