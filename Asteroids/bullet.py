import pygame

from .constants import WHITE
from .constants import DISPLAY_HEIGHT, DISPLAY_WIDTH
from .constants import BULLET_SIZE, BULLET_SPEED, BULLET_LIFESPAN

class Bullet:
     def __init__(self, location, vector):
          self.location = pygame.Vector2(location)
          self.velocity = pygame.Vector2(vector)
          self.velocity.scale_to_length(BULLET_SPEED)

          self.size = BULLET_SIZE
          self.lifespan = BULLET_LIFESPAN
     
     def update(self):
          self.location += self.velocity
          self.lifespan -= 1

          self._check_location_bounds()

     def display(self, win):
          for col in range(-1, 2):
               for row in range(-1, 2):
                    spot = (self.location.x + col*DISPLAY_WIDTH, self.location.y + row*DISPLAY_HEIGHT)
                    self._draw(spot, win)
     
     def _draw(self, location, win):
          pygame.draw.circle(win, WHITE, location, self.size)
     
     def _check_location_bounds(self):
          if self.location.x < 0:
               self.location.x += DISPLAY_WIDTH
          if self.location.x > DISPLAY_WIDTH:
               self.location.x -= DISPLAY_WIDTH

          if self.location.y < 0:
               self.location.y += DISPLAY_HEIGHT
          if self.location.y > DISPLAY_HEIGHT:
               self.location.y -= DISPLAY_HEIGHT

     def is_dead(self):
          if self.lifespan < 0:
               return True
          return False