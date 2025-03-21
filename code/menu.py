#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect #importou a variável Surface e Rect
from pygame .font import Font #importou a variável Font referente a fonte de texto

from code.const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION  # variáveis CONSTANTES


class Menu:
    def __init__(self, window): #método construtor ativado
        self.window = window #chamando a janela do manu
        self.surf = pygame.image.load('./asset/menu/Menu.png') #a imagem está sendo carregada para dentro do pygame #entre aspas simples pois é string
        self.rect = self.surf.get_rect(left=0, top=0) #self.rect vai armazenar um retângulo com a dimensão do self.surf naquela localidade

    def run(self, ):
        pygame.mixer_music.load('./asset/sounds/Menu_Sound.wav') #carrega a música de menu
        pygame.mixer_music.play(-1) #para tocar a música, parâmetro -1 para a música tocar infinitamente
        while True: #precisa desse loop para carregar a imagem
            self.window.blit(source=self.surf, dest=self.rect)  # self.window.blit = ta vindo da nossa janela, source=self.surf = que está vindo da nossa imagem, dest=self.rect = que está destacando a imagem e fazendo ela aparecer
            self.menu_text(50, "Mountain", COLOR_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_WHITE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)): #o código está percorrendo a lista e colocando TODOS os elementos referentes ao MENU_OPTION
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i)) #os textos vão sair com esta formatação e para palavra será acrescentado um espaçamento automático de 25 entre cada uma

            pygame.display.flip()  # a imagem estã sendo ATUALIZADA e aparecendo na tela

            #é o trecho de código que tira o "bug" da janela, agora ela fecha com mais facilidade
            # Check for all events (Cheque por TODOS os eventos)
            for event in pygame.event.get():  # TODOS os EVENTOS VIRÃO
                if event.type == pygame.QUIT:  # Quando o evento for do tipo quit
                    pygame.quit()  # Close Window (Fecha a janela)
                    quit()  # end pygame (Fecha de fato o pygame)

    #MÉTODO de configurações de texto no menu
    #OBS: TODO e QUALQUER texto ele se passa por uma "imagem", é o que o código entende
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size) #fonte que vamos utilizar
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() #através dessa fonte ele cria um render, ou seja, renderiza a imagem e a partir dela ele cria/vira uma Surface (Imagem)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos) #retângulo
        self.window.blit(source=text_surf, dest=text_rect) #blit da origem pro destino onde realmente desenha a imagem