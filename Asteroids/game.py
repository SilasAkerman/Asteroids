import pygame
import time
import random

from .ship import Ship
from .rock import Rock

from .constants import DISPLAY_HEIGHT, DISPLAY_WIDTH
from .constants import BLACK
from .constants import PUSH_FORCE, ROTATION_FORCE
from .constants import ROCK_AMOUNT, ROCK_SIZE_MIN, ROCK_SIZE_MAX, ROCK_INIT_ANGLE_THRESHOLD
from .constants import ROCK_SIZE_LIMIT, ROCK_POINTS_MULTIPLIER

class Game:
     def __init__(self):
          self.Ship = Ship((DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2))
          self.Asteroids = []
          self.Bullets = []

          self.game_over = False
          self.score = 0


     def push_player_forward(self):
          self.Ship.forward_force(PUSH_FORCE)

     def rotate_player(self, direction):
          if direction == "left":
               force_ang = ROTATION_FORCE * -1
          else:
               force_ang = ROTATION_FORCE
          self.Ship.add_force_ang(force_ang)

     def player_shoot(self):
          self.Bullets.append(self.Ship.shoot())


     def _generate_new_rock(self):
          # I think this could be done by chosing one quadrant of the sqrueen randomly,
          # then choose a random coordinate within that quadrant,     # don't do this
          # and lastly chose a vector aimed at the center with a random rotation
          # Order might be changed, also don't forget a random size
          coordinate = pygame.Vector2((DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2))

          quadrant = random.randint(0, 9)
          if quadrant == 4: # Middle, no want
               self._generate_new_rock()
               return

          coordinate.x += (quadrant%3 - 1) * DISPLAY_WIDTH
          coordinate.y += (quadrant//3 - 1) * DISPLAY_HEIGHT

          vector = pygame.Vector2((DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)) - coordinate

          angle = (random.random()*2 - 1) * ROCK_INIT_ANGLE_THRESHOLD/2
          vector.rotate_ip_rad(angle)

          size = random.randrange(ROCK_SIZE_MIN, ROCK_SIZE_MAX)

          self.Asteroids.append(Rock(coordinate, vector, size))


     def update(self, win):
          if len(self.Asteroids) < ROCK_AMOUNT:
               self._generate_new_rock()

          self.Ship.update()

          for asteroid in self.Asteroids:
               asteroid.update()
          for bullet in self.Bullets:
               bullet.update()

          self._check_asteroids_hit()
          self._check_player_hit()
          self._check_bullets_lifespan()

          self.draw(win)
     
     def draw(self, win):
          win.fill(BLACK)
          self.Ship.display(win)

          for asteroid in self.Asteroids:
               asteroid.display(win)
          for bullet in self.Bullets:
               bullet.display(win)


     def end_game(self):
          self.game_over = True


     def _check_asteroids_hit(self):
          for j in range(len(self.Bullets)-1, -1, -1):
               bullet = self.Bullets[j]
               for i in range(len(self.Asteroids)-1, -1, -1):
                    asteroid = self.Asteroids[i]
                    distance = asteroid.location - bullet.location
                    if distance.length() < asteroid.size + bullet.size:
                         self.score += int(ROCK_POINTS_MULTIPLIER//(asteroid.size**2)) # smaller asteroids generate more points
                         self.Asteroids.extend(asteroid.spawn_smaller_asteroids())

                         self.Asteroids.pop(i)
                         self.Bullets.pop(j)
                         break

                         print (self.score)


     def _check_player_hit(self):
          # If this is true, turn self.game_over = True
          for asteroid in self.Asteroids:
               distance = self.Ship.location - asteroid.location
               if distance.length() < asteroid.size + self.Ship.size:
                    self.end_game()

     def _check_bullets_lifespan(self):
          for i in range(len(self.Bullets)-1, -1, -1):
               if self.Bullets[i].is_dead():
                    self.Bullets.pop(i)