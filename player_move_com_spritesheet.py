import pygame
import sys

from spritesheet_explicada import SpriteSheet
from sprite_teste_v2 import Personagem

pygame.init()

screen = pygame.display.set_mode((800, 600))  # Cria uma janela de 400x300 pixels
clock = pygame.time.Clock()  # Inicializa o relógio do jogo para controlar a taxa de quadros

omori_sprite_sheet = SpriteSheet("omori_sprites/PC Computer - Omori - Omori.png", 0, 15, 32, 32, 4,[3,3,3,3], (0, 0, 0))
basil_sprite_sheet = SpriteSheet("omori_sprites/PC Computer - Omori - Basil Dream.png", 0, 0, 32, 32, 0,[3,3,3,3],(0,0,0),multiplas_linhas=False)

novo_sprite = SpriteSheet("omori_sprites\Download5005.png", 0, 512, 64, 64, 4,[6,6,6,6], (0, 0, 0))
# Cria o objeto player utilizando a classe Personagem e a imagem inicial
player = Personagem(novo_sprite)

# Grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

run = True  # Variável de controle do loop principal
while run:

    clock.tick(60)  # Limita a atualização para 3 FPS (controla a velocidade da animação)

    screen.fill((100, 100, 100))  # Preenche o fundo com uma cor sólida

    #print(player.sheet.action)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.direction = 'UP'
    elif keys[pygame.K_DOWN]:
        player.direction = 'DOWN'
    elif keys[pygame.K_LEFT]:
        player.direction = 'LEFT'
    elif keys[pygame.K_RIGHT]:
        player.direction = 'RIGHT'
    else:
        player.direction = None  # Nenhuma direção se nenhuma tecla for pressionada


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.direction = None
            elif event.key == pygame.K_DOWN:
                player.direction = None
            elif event.key == pygame.K_LEFT:
                player.direction = None
            elif event.key == pygame.K_RIGHT:
                player.direction = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.nova_direcao = True
            elif event.key == pygame.K_DOWN:
                player.nova_direcao = True
            elif event.key == pygame.K_LEFT:
                player.nova_direcao = True
            elif event.key == pygame.K_RIGHT:
                player.nova_direcao = True
    # Atualiza os sprites
    all_sprites.update()

    # Renderiza o jogador
    #all_sprites.draw(screen)

    player.sheet.draw(screen, player.rect.x, player.rect.y)
    #print("Posição do player:", player.rect.x, player.rect.y)
    #print(player.sheet.index)

    #player.sheet.draw(screen, player.rect.x, player.rect.y)  # Desenha o sprite no centro da tela
    pygame.display.update()  # Atualiza a tela com as novas imagens
