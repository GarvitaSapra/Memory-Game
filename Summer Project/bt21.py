import random 
import os
import game_config as gc

from pygame import image, transform

toons_count = dict((a, 0) for a in gc.img_files)

def available_toons():
      return [a for a , c in toons_count.items() if c<2]

class bts:
     def __init__(self, index):
          self.index = index
          self.name = random.choice(available_toons())
          self.image_path = os.path.join(gc.IMG_DIR, self.name)
          self.row = index // gc.NUM_TILES_SIDE
          self.col = index % gc.NUM_TILES_SIDE
          self.skip = False
          self.image = image.load(self.image_path)
          self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
          self.box = self.image.copy()
          self.box.fill((128, 0, 255))

          toons_count[self.name] +=1   

      


