#Создай собственный Шутер!
from pygame import *
from random import randint
from time import time as trtrt

#создай окно игры
window = display.set_mode((700,500))
display.set_caption('ААААААААААА')
clock = time.Clock()
FPS = 60

font.init()
font2 = font.SysFont("Arial", 36)
font3 = font.SysFont("Arial", 100)

#музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

#классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, rx, ry):
        super().__init__()
        self.rx = rx
        self.ry = ry
        self.image = transform.scale(image.load(player_image), (rx, ry))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def xodim(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 8
        if keys_pressed[K_RIGHT] and self.rect.x < 610:
            self.rect.x += 8

    def strelyaem(self): 
        global pulya
        pulya = Bullit('bullet.png', self.rect.centerx, self.rect.top, 1, 20, 10)
        bullets.add(pulya)

pop = 0
nopop = 0
nooooon = 0
class Enemy(GameSprite):
    def update(self):
        if self.rect.y <= 470:
            self.speed = abs(self.speed)
        self.rect.y += self.speed
        num_x = randint(0, 650)
        global pop
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = num_x
            self.speed = 1
            pop += 1

class Sssss(GameSprite):
    def update(self):
        if self.rect.y <= 470:
            self.speed = abs(self.speed)
        self.rect.y += self.speed
        num_x = randint(0, 650)
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = num_x
            self.speed = 1
            

class Bullit(GameSprite):
    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()

#в общем создаём 
#фон/сприте/и тд тп
num_x = randint(0, 650)

background = transform.scale(image.load('galaxy.jpg'), (700, 500))
hero = Player('rocket.png', 250, 400, 10, 70, 100)

all_sprites = sprite.Group()
for i in range(5):
    global mons
    mons = Enemy('ufo.png', num_x, 0, 1, 70, 40)
    all_sprites.add(mons)

aaaaaaaaaaall = sprite.Group()
for i in range(3):
    global actr
    actr = Sssss('asteroid.png', num_x, 0, 2, 70, 40)
    aaaaaaaaaaall.add(actr)

bullets = sprite.Group()

#занимательный баг: колайдер работает только тогда, 
#когда тарелка касается ракеты во время её движения

#игровой цикл
real_time = False
num_fire = 0 
finish = False
game = True
game_over = False
while game:
    if game_over == False:
        window.blit(background, (0, 0))
        hero.reset()
        all_sprites.draw(window)
        aaaaaaaaaaall.draw(window)

        bullets.draw(window)
        bullets.update()

        hero.xodim()
        all_sprites.update()
        aaaaaaaaaaall.update()
        popi = font2.render('Пропустил: ' + str(pop), True, (255, 255, 255))
        window.blit(popi, (0, 30))
        nopopi = font2.render('Счёт: ' + str(nopop), True, (255, 255, 255))
        window.blit(nopopi, (0, 1))

        if real_time==True:
                    nou_ti = trtrt()
                    if nou_ti - u<3:
                        p=font2.render('Патроны кончились..', 1, (150, 0, 0))
                        window.blit(p, (260, 460))
                    else:
                        num_fire=0
                        real_time = False

    #оаоаооаоаоа столкновенияяяяяяяяяяяяя

    if sprite.spritecollide(hero, all_sprites, False):
        sss = font3.render('вы погибли', True, (255, 0, 0))
        window.blit(sss, (165, 200))
        game_over = True
    if sprite.groupcollide(all_sprites, bullets, True, True):
        nopop += 1
        num_x = randint(0, 650)
        mons = Enemy('ufo.png', num_x, 0, 1, 70, 40)
        all_sprites.add(mons)

    if nopop == 10:
        game_over = True
        ss1 = font3.render('победа?', True, (255, 0, 0))
        window.blit(ss1, (195, 230))
    if pop == 7:
        game_over = True
        ss2 = font3.render('oh nooo', True, (255, 0, 0))
        window.blit(ss2, (205, 230))


    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type ==  KEYDOWN:
            if e.key == K_SPACE:
                if num_fire <5 and real_time==False:
                    num_fire+=1
                    hero.strelyaem()
                if num_fire>=5 and real_time==False:
                    real_time = True
                    u = trtrt() 

    clock.tick(FPS)
    display.update()