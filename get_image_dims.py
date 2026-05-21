from PIL import Image

img = Image.open('Projects/header image.png')
width = img.width
height = img.height
aspect_ratio = width / height

print(f'Header Image Dimensions:')
print(f'Width: {width}px')
print(f'Height: {height}px')
print(f'Aspect Ratio: {aspect_ratio:.4f}')
