import pygame #importando a biblioteca pygame

from code.menu import Menu #importando o menu

# !/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()  # INICIALIZAÇÃO do programa
        self.window = pygame.display.set_mode(size=(600, 480))  # Seria a nossa janela de jogo em si

    def run(self):
        while True:  # A janela fica aberta infinitamente
            menu = Menu(self.window) #chamando a janela do menu
            menu.run() #rodando o menu
            pass

            # Check for all events (Cheque por TODOS os eventos)
            # for event in pygame.event.get():  # TODOS os EVENTOS VIRÃO
            #    if event.type == pygame.QUIT:  # Quando o evento for do tipo quit
            #        pygame.quit()  # Close Window (Fecha a janela)
            #        quit()  # end pygame (Fecha de fato o pygame)
