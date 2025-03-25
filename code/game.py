import pygame #importando a biblioteca pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION  # arquivos constantes do menu importados
from code.level import Level
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
            menu_return = menu.run() #variável recebe o retorno do menu

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: #se MENU_OPTION for = a opção 0, 1 ou 2
                level = Level(self.window, 'Level1', menu_return) #chama o Level1
                level_return = level.run() #roda o Level1
            elif menu_return == MENU_OPTION[4]: #se MENU_OPTION for = a 4
                pygame.quit()  # Close Window (Fecha a janela)
                quit()  # end pygame (Fecha de fato o pygame)
            else:
                pass