import pygame #importando a biblioteca pygame

from code.const import WIN_WIDTH, WIN_HEIGHT #arquivos constantes do menu importados
from code.menu import Menu #importando o menu

# !/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()  # INICIALIZAÇÃO do programa
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Seria a nossa janela de jogo em si (Tamanho dela/imagem)

    def run(self):
        while True:  # A janela fica aberta infinitamente
            menu = Menu(self.window) #chamando a janela do menu
            menu.run() #rodando o menu
            pass #é um preenchimento vazio que não faz nada, é usada quando um bloco de código é obrigatório, mas ainda não quer ou não precisa definir nenhuma lógica.


