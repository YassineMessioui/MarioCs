import pygame
from settings import *


class GUI:
    def __init__(self, screen):

        # setup
        self.display_screen = screen

        # health
        self.health = [pygame.image.load('./graphics/hearts/0heart.png').convert_alpha(),
                       pygame.image.load(
                           './graphics/hearts/1heart.png').convert_alpha(),
                       pygame.image.load(
                           './graphics/hearts/2hearts.png').convert_alpha(),
                       pygame.image.load(
                           './graphics/hearts/3hearts.png').convert_alpha()
                       ]
        self.health_3 = pygame.transform.scale_by(self.health[3], 0.5)
        self.health_2 = pygame.transform.scale_by(self.health[2], 0.5)
        self.health_1 = pygame.transform.scale_by(self.health[1], 0.5)
        self.health_0 = pygame.transform.scale_by(self.health[0], 0.5)

        # coins
        self.coin_gold = pygame.image.load('./graphics/coins/gold/0.png')
        self.coin_silver = pygame.image.load('./graphics/coins/silver/0.png')
        self.coin_gold_rect = self.coin_gold.get_rect(topleft=(30, 47))
        self.coin_silver_rect = self.coin_silver.get_rect(topleft=(30, 75))
        self.font_gold = pygame.font.Font('./graphics/coins/ARCADEPI.ttf', 30)
        self.font_silver = pygame.font.Font(
            './graphics/coins/ARCADEPI.ttf', 30)

        # tagine
        self.tagine = pygame.image.load('./graphics/character/tajine.png')
        self.tagine_rect = self.tagine.get_rect(topleft=(1170, 12))
        self.font_tagine = pygame.font.Font(
            './graphics/coins/ARCADEPI.ttf', 30)

        # score
        self.font_score = pygame.font.Font('./graphics/coins/ARCADEPI.ttf', 30)
        self.font_score_count = pygame.font.Font(
            './graphics/coins/ARCADEPI.ttf', 30)
        self.font_high_score = pygame.font.Font(
            './graphics/coins/ARCADEPI.ttf', 70)
        # Congrats
        self.font_congrats = pygame.font.Font(
            './graphics/coins/ARCADEPI.ttf', 50)

    def show_health(self, current):
        self.hearts = [self.health_0, self.health_1,
                       self.health_2, self.health_3]
        self.display_screen.blit(self.hearts[current], (20, 10))

    def show_coins(self, amount):
        g, s = amount
        self.display_screen.blit(self.coin_gold, self.coin_gold_rect)
        self.display_screen.blit(self.coin_silver, self.coin_silver_rect)
        coing_amount_surf = self.font_gold.render(str(g), False, '#33323d')
        coins_amount_surf = self.font_silver.render(str(s), False, '#33323d')
        coing_amount_rect = coing_amount_surf.get_rect(
            midleft=(self.coin_gold_rect.right + 4, self.coin_gold_rect.centery))
        coins_amount_rect = coins_amount_surf.get_rect(
            midleft=(self.coin_silver_rect.right + 4, self.coin_silver_rect.centery))
        self.display_screen.blit(coing_amount_surf, coing_amount_rect)
        self.display_screen.blit(coins_amount_surf, coins_amount_rect)

    def show_tagine(self, amount):
        self.display_screen.blit(self.tagine, self.tagine_rect)
        tagine_amount_surf = self.font_gold.render(
            str(amount), False, '#33323d')
        tagine_amount_rect = tagine_amount_surf.get_rect(
            midleft=(self.tagine_rect.right + 4, self.tagine_rect.centery))
        self.display_screen.blit(tagine_amount_surf, tagine_amount_rect)

    def show_score(self, amount):
        score_amount_surf = self.font_score_count.render(
            str(amount), False, '#33323d')
        score_surf = self.font_score.render("SCORE", False, '#33323d')
        score_rect = score_surf.get_rect(topleft=(480, 10))
        score_amount_rect = score_amount_surf.get_rect(topleft=(650, 10))
        self.display_screen.blit(score_amount_surf, score_amount_rect)
        self.display_screen.blit(score_surf, score_rect)

    def show_high_score(self, high_score, current_score):
        high_score_surf = self.font_high_score.render(
            'High Score : ' + str(high_score), False, '#ffffff')
        high_score_rect = high_score_surf.get_rect(
            center=(screen_width//2, 100))
        current_score_surf = self.font_high_score.render(
            'Score : ' + str(current_score), False, '#ffffff')
        current_score_rect = current_score_surf.get_rect(
            center=(screen_width//2, 200))
        self.display_screen.blit(high_score_surf, high_score_rect)
        self.display_screen.blit(current_score_surf, current_score_rect)

    def show_Congrats(self):
        congrats_surf = self.font_congrats.render(
            'Congratulations you won the game ', False, '#ffffff')
        congrats_rect = congrats_surf.get_rect(
            center=(screen_width//2, 100))
        self.display_screen.blit(congrats_surf, congrats_rect)
