import os
try:
    from PIL import Image
    img = Image.open('Projects/header-image.png')
    width = img.width
    height = img.height
    print(f'Header Image: {width}x{height}px, Aspect: {width/height:.4f}')
except ImportError:
    # Fallback - read file info
    file_size = os.path.getsize('Projects/header-image.png')
    print(f'File size: {file_size} bytes')
