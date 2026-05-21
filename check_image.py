from PIL import Image

img = Image.open('Projects/header image.jfif')
print(f'Width: {img.width}px, Height: {img.height}px, Aspect Ratio: {img.width/img.height:.2f}')
