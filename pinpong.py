from pygame import *
game = True
wndw = display.set_mode((600, 500))
wndw.fill((255, 255, 255))
clock = time.Clock()
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        wndw.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
class Player(GameSprite):
    def updater(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed

pl1 = Player('ракоетка.png', 100, 100, 40, (150, 25))
pl2 = Player('ракоетка.png', 100, 100, 40, (150, 25))




while game != False:
    for e in event.get():
        if e.type == QUIT:
            game = False  


    
    
    
    display.update()
    clock.tick(60)
