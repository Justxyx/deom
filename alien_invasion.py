import pygame
import game_function as gf
from settings import Setting
from ship import Ship
from pygame.sprite import Group
from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)

    alien = Alien(ai_settings,screen)



    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.updata()
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)
        gf.updata_bullets(aliens,bullets)
        gf.updata_aliens(ai_settings,aliens)


run_game()


