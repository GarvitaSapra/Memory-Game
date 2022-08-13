import os

IMAGE_SIZE = 175
SCREEN_SIZE = 700
NUM_TILES_SIDE = 4
NUM_TILES_TOTOAL = 16
MARGIN = 8

IMG_DIR = 'bt21'
img_files = [x for x in os.listdir(IMG_DIR) if x[-3:].lower() == 'png']
assert len(img_files) == 8
