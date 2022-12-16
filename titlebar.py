import pygame
from constants import *
from utils import *
from assetloader import AssetLoader
from board import Board
from diffselect import DifficultySelector


class Titlebar:
    def __init__(self):
        self.image = load_image("controls.png")
        self.minimize_hovered = load_image("minimize-hovered.png")
        self.minimize_location = (1012-30, 10)
        self.refresh_hovered = load_image("refresh-hovered.png")
        self.refresh_location = (1044-30, 12)
        self.close_hovered = load_image("close-hovered.png")
        self.close_location = (1044, 12)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (0, 0))
        minimize_rect = self.minimize_hovered.get_rect(topleft=self.minimize_location)
        refresh_rect = self.refresh_hovered.get_rect(topleft=self.refresh_location)
        close_rect = self.close_hovered.get_rect(topleft=self.close_location)
        if minimize_rect.collidepoint(mp()):
            screen.blit(self.minimize_hovered, self.minimize_location)
        if refresh_rect.collidepoint(mp()):
            screen.blit(self.refresh_hovered, self.refresh_location)
        if close_rect.collidepoint(mp()):
            screen.blit(self.close_hovered, self.close_location)

    def handle_event(self, event: pygame.event.Event):
        minimize_rect = self.minimize_hovered.get_rect(topleft=self.minimize_location)
        refresh_rect = self.refresh_hovered.get_rect(topleft=self.refresh_location)
        close_rect = self.close_hovered.get_rect(topleft=self.close_location)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if minimize_rect.collidepoint(mp()):
                    pygame.display.iconify()
                if refresh_rect.collidepoint(mp()):
                    DifficultySelector.instance.shown = True
                    AssetLoader.play_sound(AssetLoader.select_sound)
                if close_rect.collidepoint(mp()):
                    pygame.quit()
                    quit()
