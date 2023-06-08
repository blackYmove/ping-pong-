from pygame import *
game = True
wndw = display.set_mode((600, 500))
wndw.fill((255, 255, 255))
clock = time.Clock()
finish = False
speed_x = 3
speed_y = 3
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
        if keys[K_s] and self.rect.y < 340:
            self.rect.y += self.speed
    def updater(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 340:
            self.rect.y += self.speed

pl1 = Player('ракоетка.png', 550, 100, 4, (25, 150))
pl2 = Player('ракоетка.png', 5, 100, 4, (25, 150))
myach = GameSprite('мяч.png', 250, 250, 5, (50,50))
font.init()
fontt = font.Font(None, 35)
win1 = fontt.render('игрок 1 победил', True, (180, 0, 0))
win2 = fontt.render('игрок 2 победил', True, (180, 0, 0)) 

while game != False:
    
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        wndw.fill((255, 255, 255))
        myach.rect.x += speed_x
        myach.rect.y += speed_y
        pl1.updater()
        pl1.reset()
        pl2.updatel()
        pl2.reset()
        myach.reset()
    if myach.rect.y > 450 or myach.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(pl1, myach) or sprite.collide_rect(pl2, myach):
        speed_x *= -1
    if myach.rect.x < 0:
        finish = True
        wndw.blit(win1, (200, 200))
    if myach.rect.x > 550:
        finish = True
        wndw.blit(win2, (200, 200))


    
    
    
    display.update()
    clock.tick(60)
