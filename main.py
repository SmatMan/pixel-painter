import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
)

resolution = (800, 800)

pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
pygame.key.set_repeat(0, 500)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imageSize = (50, 50)
        self.image = pygame.Surface(self.imageSize)
        #self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = (resolution[0]-self.imageSize[0]) / 2
        self.rect.y = (resolution[1]-self.imageSize[1]) / 2 
        
        self.speed = 50
    def updatePosition(self, event):
        print(event.key)
        if event.key == K_UP and self.rect.y > 0:
            self.rect.y -= self.speed
        elif event.key == K_DOWN and self.rect.y < resolution[1] - self.imageSize[1]:
            self.rect.y += self.speed
        elif event.key == K_LEFT and self.rect.x > 0:
            self.rect.x -= self.speed
        elif event.key == K_RIGHT and self.rect.x < resolution[0] - self.imageSize[0]:
            self.rect.x += self.speed
        


class Block(pygame.sprite.Sprite):
    def __init__(self, colour=(4, 41, 27), size=(50, 50), location=(0, 0)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            player.updatePosition(event)
            if event.key == pygame.K_e:
                block = Block(location=(player.rect.x, player.rect.y))
                all_sprites.add(block)
            if event.key == pygame.K_q:
                for i in all_sprites:
                    if i.rect.x == player.rect.x and i.rect.y == player.rect.y and not isinstance(i, Player):
                        all_sprites.remove(i)

    screen.fill((255, 255, 255))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
