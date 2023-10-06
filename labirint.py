from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_width=65, image_height=65):
        super().__init__()
        self.image_width = image_width
        self.image_height = image_height
        self.image = transform.scale(image.load(player_image), (image_width, image_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < x-70:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < y-70:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def enemy_move(self):
        self.rect.x += self.speed
        if self.rect.x > x-70 or self.rect.x < x-200:
            self.speed *= -1

class Enemy2(GameSprite):
    def enemy_move2(self):
        self.rect.x += self.speed
        if self.rect.x > x-555 or self.rect.x < 5:
            self.speed *= -1


sprite1 = Player('hero.png', 20, 450, 1.5)
sprite2 = Enemy('cyborg.png', 600, 280, 1)
sprite3 = Enemy2('cyborg.png', 5, 151, 1)
wall1 = GameSprite('фон джунгли.jpg', 200, 100, 0, 15, 450) 
wall2 = GameSprite('фон джунгли.jpg', 325, 0, 0, 15, 385)
wall3 = GameSprite('фон джунгли.jpg', 450, 100, 0, 15, 450)
wall4 = GameSprite('фон джунгли.jpg', 110, 100, 0, 100, 15)
treasure = GameSprite('treasure.png', 555, 401) 


x = 700
y = 500
window = display.set_mode((x, y))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (x, y))


font.init()
font = font.Font(None, 70)
mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()



end = True
game = True
while game:
    if end:
        window.blit(background, (0, 0))
        sprite2.reset()
        sprite1.move()
        sprite1.reset()
        sprite2.enemy_move()
        sprite3.reset()
        sprite3.enemy_move2()
        wall1.reset()
        wall2.reset()
        wall3.reset()
        wall4.reset()
        treasure.reset()
        if (sprite.collide_rect(sprite1, sprite2) or sprite.collide_rect(sprite1, wall1) 
        or sprite.collide_rect(sprite1, wall2) or sprite.collide_rect(sprite1, wall3) 
        or sprite.collide_rect(sprite1, wall4) or sprite.collide_rect(sprite1, sprite3)):
            kick = mixer.Sound('kick.ogg')
            kick.play()
            lose = font.render('YOU LOSE!', True, (255, 215,0))
            window.blit(lose, (200, 250))
            end = False
        if sprite.collide_rect(sprite1, treasure):
            money = mixer.Sound('money.ogg')
            money.play()
            win = font.render('YOU WIN!', True, (255, 215,0))
            window.blit(win, (230, 250))
            end = False
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()




