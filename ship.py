import pygame


class Ship:
    def __init__(self, ai_settins, screen):
        self.screen = screen
        self.setings = ai_settins

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.setings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.setings.ship_speed_factor
        if self.moving_up:
            self.rect.bottom -= self.setings.ship_speed_factor
        if self.moving_down:
            self.rect.bottom += self.setings.ship_speed_factor

        self.rect.centerx = self.center
