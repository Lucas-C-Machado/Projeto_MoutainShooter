from abc import ABC, abstractmethod
import pygame


class Entity (ABC): #classe ABC = Classe ABSTRATA

    def __init__(self, name: str, position: tuple ): #vai definir um nome e uma posição
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod #decorator
    def move (self, ):
        pass