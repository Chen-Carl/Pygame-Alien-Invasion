import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)

    # set background color
    bg_color = (230, 230, 230)
    # create a ship
    ship = Ship(ai_settings, screen)
    # create a group of bullets
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        # supervise events from mouse and keyboard
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
                        bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats,
                         play_button)


run_game()