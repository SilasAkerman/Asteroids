import pygame
import random

from .constants import DISPLAY_HEIGHT, DISPLAY_WIDTH
from .constants import ROCK_SPEED, ROCK_WIDTH
from .constants import WHITE
from .constants import ROCK_SIZE_DIVISION_RANGE, ROCK_SIZE_DIVISION_AMOUNT
from .constants import ROCK_ANGLE_DIVISION_RANGE, ROCK_SIZE_LIMIT

class Rock:
     def __init__(self, location, velocity, size):
          self.location = pygame.Vector2(location)
          self.velocity = pygame.Vector2(velocity)
          self.velocity.scale_to_length(ROCK_SPEED)

          self.size = size
          self.shown = False

     def update(self):
          self.location += self.velocity

          if self.shown:
               self._check_location_bounds()
          else:
               self.shown = self._check_if_shown()

     def display(self, win):
          if self.shown:
               for col in range(-1, 2):
                    for row in range(-1, 2):
                         spot = (self.location.x + col*DISPLAY_WIDTH, self.location.y + row*DISPLAY_HEIGHT)
                         self._draw(spot, win)
          else:
               self._draw(self.location, win)
     
     def _draw(self, location, win):
          pygame.draw.circle(win, WHITE, location, self.size, ROCK_WIDTH)
     
     def _check_location_bounds(self):
          if self.location.x < 0:
               self.location.x += DISPLAY_WIDTH
          if self.location.x > DISPLAY_WIDTH:
               self.location.x -= DISPLAY_WIDTH

          if self.location.y < 0:
               self.location.y += DISPLAY_HEIGHT
          if self.location.y > DISPLAY_HEIGHT:
               self.location.y -= DISPLAY_HEIGHT


     def spawn_smaller_asteroids(self):
          # Called by the game object, returns two smaller rock objects
          new_asteroids = []

          for i in range(ROCK_SIZE_DIVISION_AMOUNT):
               velocity = self.velocity.rotate_rad((random.random()*2-1) * (ROCK_ANGLE_DIVISION_RANGE/2))
               size = self.size / random.choice(ROCK_SIZE_DIVISION_RANGE)
               if size >= ROCK_SIZE_LIMIT:
                    new_rock = Rock(self.location, velocity, size)
                    new_rock.shown = True
                    new_asteroids.append(new_rock)

          return new_asteroids

     def _check_if_shown(self):
          # We are going to check if the entire circle is contained in the display window
          inner_box_x1 = self.size * 2
          inner_box_y1 = self.size * 2
          inner_box_x2 = DISPLAY_WIDTH - self.size*2
          inner_box_y2 = DISPLAY_HEIGHT - self.size*2

          if (self.location.x > inner_box_x1 and self.location.x < inner_box_x2) and (self.location.y > inner_box_y1 and self.location.y < inner_box_y2):
               return True
          return False