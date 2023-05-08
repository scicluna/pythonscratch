import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:  # iterate over sys.argv starting at 1
    image = Image.open(arg)  # open the image file
    images.append(image)

images[0].save(
    # shit ton of pillow boilerplate and settings. whatever
    # append image one to it, and change every 200 ms.
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
