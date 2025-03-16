import pygame

print('Setup Start')  # Informa ao usuário que um processo de CONFIGURAÇÃO está INICIANDO
pygame.init()  # INICIALIZAÇÃO do programa
window = pygame.display.set_mode(size=(600, 480))  # Seria a nossa janela de jogo em si
# CTRL + ALT + L = Corrige a formatação de TODO o código
print('Setup End')  # Informa ao usuário que um processo de CONFIGURAÇÃO está TERMINANDO

print('Loop Start')  # Informa ao usuário que um processo de LOOP está INICIANDO
while True:  # A janela fica aberta infinitamente
    # Check for all events (Cheque por TODOS os eventos)
    for event in pygame.event.get():  # TODOS os EVENTOS VIRÃO
        if event.type == pygame.QUIT: #Quando o evento for do tipo quit
            pygame.quit()  # Close Window (Fecha a janela)
            quit()  # end pygame (Fecha de fato o pygame)
