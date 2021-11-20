from Asteroids.constants import DISPLAY_HEIGHT, DISPLAY_WIDTH, FPS, GUN_COOLDOWN, END_COOLDOWN
from Asteroids.game import Game
from Asteroids import ui

import pygame
import time

def main():
     pygame.init()

     WIN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

     Clock = pygame.time.Clock()

     Asteroids = Game()

     gun_timer = float("-inf")
     end_timer = -1        

     while True:
          Clock.tick(FPS)
          keys = pygame.key.get_pressed()

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()

               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                         pygame.quit()
                    if event.key == pygame.K_r:
                         main()

                    if event.key == pygame.K_SPACE and not Asteroids.game_over:
                         if GUN_COOLDOWN <= 0:
                              Asteroids.player_shoot()


          if not Asteroids.game_over:
               if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    # Left rotation
                    Asteroids.rotate_player("left")

               if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    # Right rotation
                    Asteroids.rotate_player("right")

               if keys[pygame.K_UP] or keys[pygame.K_w]:
                    # Forward momentum
                    Asteroids.push_player_forward()
               
               if keys[pygame.K_SPACE] and not GUN_COOLDOWN <= 0 :
                    if time.time() - gun_timer > GUN_COOLDOWN:
                         Asteroids.player_shoot()
                         gun_timer = time.time()


          Asteroids.update(WIN)

          if Asteroids.game_over:
               if end_timer < 0:
                    end_timer = time.time()
                    ui.draw_score(WIN, Asteroids.score)
               elif time.time() - end_timer > END_COOLDOWN:
                    ui.draw_end_screen(WIN, Asteroids.score)
               else:
                    ui.draw_score(WIN, Asteroids.score)
          else:
               ui.draw_ui(WIN, Asteroids.score, gun_timer)

          pygame.display.update()


if __name__ == "__main__":
     main()