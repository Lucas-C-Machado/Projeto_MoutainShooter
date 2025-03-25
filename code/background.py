#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple): #método construtor
        super().__init__(name, position) #superclasse

    def move(self, ):
        pass
