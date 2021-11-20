import pygame
import math

from .bullet import Bullet

from .constants import DISPLAY_WIDTH, DISPLAY_HEIGHT
from .constants import SHIP_VERTECIES, SHIP_SIZE, SHIP_LINE_WIDTH
from .constants import WHITE
from .constants import RECOIL_FORCE, ROTATION_DRAG, DRAG_FORCE

class Ship:
     def __init__(self, location):
          self.location = pygame.Vector2(location)
          self.velocity = pygame.Vector2()
          self.acceleration = pygame.Vector2()

          self.angle = math.pi/2 # rotation clockwise
          self.angle_vel = 0
          self.angle_acc = 0

          self.size = SHIP_SIZE


     def forward_force(self, push):
          force = push.copy()
          force = self._rotate_vertex(force, self.angle)

          self.add_force(force)


     def add_force(self, force):
          force = pygame.Vector2(force)

          self.acceleration += force

     def _apply_drag_force(self):
          if self.velocity.magnitude() == 0:
               return

          drag = self.velocity.normalize()
          drag *= self.velocity.magnitude_squared()
          drag *= -DRAG_FORCE
          self.add_force(drag)


     def add_force_ang(self, force):
          self.angle_acc += force

     def _apply_drag_force_ang(self):
          if self.angle_vel == 0:
               return

          drag_ang = 1 if self.angle_vel > 0 else -1
          drag_ang *= self.angle_vel * self.angle_vel
          drag_ang *= -ROTATION_DRAG
          self.add_force_ang(drag_ang)


     def update(self):
          self._apply_drag_force()
          self._apply_drag_force_ang()

          self.velocity += self.acceleration
          self.location += self.velocity
          self.acceleration *= 0

          self.angle_vel += self.angle_acc
          self.angle += self.angle_vel
          self.angle_acc *= 0

          self._check_location_bounds()
     
     def _check_location_bounds(self):
          if self.location.x < 0:
               self.location.x += DISPLAY_WIDTH
          if self.location.x > DISPLAY_WIDTH:
               self.location.x -= DISPLAY_WIDTH

          if self.location.y < 0:
               self.location.y += DISPLAY_HEIGHT
          if self.location.y > DISPLAY_HEIGHT:
               self.location.y -= DISPLAY_HEIGHT


     def display(self, win):
          # Might use an image or draw a tri-polygon while handling vertex rotation
          for col in range(-1, 2):
               for row in range(-1, 2):
                    spot = (self.location.x + col*DISPLAY_WIDTH, self.location.y + row*DISPLAY_HEIGHT)
                    self._draw(spot, win)

          # self._draw(self.location, win)

     
     def _draw(self, location, win):
          # This will draw in 9 places for a wrap-around effect
          points = SHIP_VERTECIES.copy()
          for index, point in enumerate(points):
               vertex = self._rotate_vertex(point, self.angle)
               vertex = (vertex[0] + location[0], vertex[1] + location[1])

               points[index] = vertex

          pygame.draw.polygon(win, WHITE, points, SHIP_LINE_WIDTH)
          # pygame.draw.circle(win, WHITE, location, self.size, SHIP_LINE_WIDTH)

     def _rotate_vertex(self, vertex, angle):
          new_vertex = [
               math.cos(angle)*vertex[0] - math.sin(angle)*vertex[1],
               math.sin(angle)*vertex[0] + math.cos(angle)*vertex[1]
          ]
          return new_vertex
     

     def shoot(self):
          # Returns the created bullet object
          ship_tip = pygame.Vector2(self._rotate_vertex(SHIP_VERTECIES[0], self.angle))
          bullet = Bullet(self.location + ship_tip, ship_tip)

          # Then the player should be pushed back slightly
          force = ship_tip * -1
          force *= RECOIL_FORCE
          self.add_force(force)

          return bullet