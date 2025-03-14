import pygame

# Classe que herda de pygame.sprite.Sprite
class Personagem(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        super().__init__()  # Chama o inicializador da classe pai
        self.sheet = sprite_sheet
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)  # A imagem inicial
        self.rect = self.image.get_rect()  # Obtém o retângulo da imagem para movimentação
        

        self.speed = 2  # Velocidade de movimento
        self.posX = 400  # Posição inicial
        self.posY = 300
        self.rect.topleft = (self.posX, self.posY)  # Define a posição inicial

        self.frame_count = 0  # Contador de frames
        self.sprite_atual = 0  # Contador para alternar entre sprites de animação
        self.direction = 'DOWN'  # Direção de movimento (cima, baixo, esquerda, direita)

        self.nova_direcao = False

    def update(self):
        # Atualiza o contador de frames
        self.frame_count += 1
        self.moving = False

        if self.direction == 'UP':
            self.sheet.action = 0
            self.rect.y -= self.speed  # Move para cima
            self.moving = True
        elif self.direction == 'DOWN':
            self.sheet.action = 2
            self.rect.y += self.speed  # Move para baixo
            self.moving = True
        elif self.direction == 'LEFT':
            self.sheet.action = 1
            self.rect.x -= self.speed  # Move para a esquerda
            self.moving = True
        elif self.direction == 'RIGHT':
            self.sheet.action = 3
            self.rect.x += self.speed  # Move para a direita
            self.moving = True

            #self.sprite_atual = (self.sprite_atual + 1) % 2
        # A cada 10 frames, troca de sprite para evitar animação rápida demais
        if self.moving:
            if self.frame_count % 10 == 0 or self.nova_direcao == True:  
                self.sheet.update()
                self.nova_direcao = False
        else:
            self.sheet.tile_rect = self.sheet.cells[self.sheet.action][1]

    def get_sprite(self):
        rect = pygame.Rect(self.sheet.tile_rect)
        sprite = pygame.Surface((32,32), pygame.SRCALPHA)
        sprite.blit(self.sheet.sheet, (0, 0), rect)
