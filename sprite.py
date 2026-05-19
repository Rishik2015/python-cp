import pygame
import random
pygame.init()
SPRITE_COLORR_CHANGE_EVENT = pygame.USERVENT + 1
BG_CHANGE_EVENT = pygame.USEREVENT + 2
 
BLUE = pygame.Color("blue")
LIGHTBLUE = pygame.Color("lightblue")
DARKBLUE = pygame.Color("darkblue")

WHITE = pygame.Color("white")
ORANGE = pygame.Color("orange")
RED = pygame.Color("red")

class Sprite(pygame.spriter.Sprite):
    def __init__(self , color , height, width):
        super().__init__()
        self.image = pygame.Surface([width ,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]

    def update(self)    :
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right>= 500:
            self.velocity[0] = - self.velocity[0]
            boundary_hit = True
        if self.rect.left <= 0 or self.rect.right>= 500:
            self.velocity[0] = - self.velocity[0]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLORR_CHANGE_EVENT))        
            pygame.event.post(pygame.event.Event(BG_CHANGE_EVENT))        
    def change_color(self)  :
        self.image.fill(random.choice([WHITE , ORANGE,RED]))      
def change_bg_color()        :
    global bg_color
    bg_color = random.choice([DARKBLUE,LIGHTBLUE,BLUE])
all_sprites_list = pygame.sprite.Group()    
sp1 = Sprite(WHITE,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("COLRFUL Bounce")
bg_color = True
screen.fill(bg_color)