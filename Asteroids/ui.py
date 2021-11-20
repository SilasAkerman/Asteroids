import pygame
import time

from .constants import GUN_COOLDOWN, WHITE
from .constants import COOLDOWN_TIMER_LOCATION, COOLDOWN_TIMER_SIZE, COOLDOWN_TIMER_WIDTH
from .constants import SCORE_FONT, SCORE_LOCATION
from .constants import GAME_OVER_FONT, GAME_OVER_LOCATION, GAME_OVER_TEXT
from .constants import MESSAGE_FONT, MESSAGE_LOCATION, MESSAGE_TEXT

def draw_score(win, score):
     score_text = SCORE_FONT.render(str(score), True, WHITE)
     score_text_location = (SCORE_LOCATION[0] - score_text.get_width(), SCORE_LOCATION[1])
     win.blit(score_text, score_text_location)

def draw_cooldown(win, gun_time):
     if GUN_COOLDOWN <= 0:
          return
          
     bar_shape = pygame.rect.Rect(COOLDOWN_TIMER_LOCATION[0], COOLDOWN_TIMER_LOCATION[1], COOLDOWN_TIMER_SIZE[0], COOLDOWN_TIMER_SIZE[1])
     cooldown_shape = _cooldown_rect(gun_time)
     pygame.draw.rect(win, WHITE, cooldown_shape)
     pygame.draw.rect(win, WHITE, bar_shape, COOLDOWN_TIMER_WIDTH)

def draw_end_screen(win, score):
     draw_score(win, score)

     game_over_text = GAME_OVER_FONT.render(GAME_OVER_TEXT, True, WHITE)
     game_over_location = (GAME_OVER_LOCATION[0] - game_over_text.get_width()/2, GAME_OVER_LOCATION[1])
     win.blit(game_over_text, game_over_location)

     message_text = MESSAGE_FONT.render(MESSAGE_TEXT, True, WHITE)
     message_location = (MESSAGE_LOCATION[0] - message_text.get_width()/2, MESSAGE_LOCATION[1])
     win.blit(message_text, message_location)

def draw_ui(win, score, gun_time):
     draw_score(win, score)
     draw_cooldown(win, gun_time)

def _cooldown_rect(gun_time):
     cooldown_percentage = (time.time() - gun_time) / GUN_COOLDOWN
     cooldown_percentage = 1 if cooldown_percentage > 1 else cooldown_percentage

     location_x = COOLDOWN_TIMER_LOCATION[0]
     location_y = COOLDOWN_TIMER_LOCATION[1] + (COOLDOWN_TIMER_SIZE[1] * (1 - cooldown_percentage))
     width = COOLDOWN_TIMER_SIZE[0]
     height = COOLDOWN_TIMER_SIZE[1] * cooldown_percentage

     return pygame.rect.Rect(location_x, location_y, width, height)