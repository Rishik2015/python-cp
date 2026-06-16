import math
import random
import pygame

sc_wid = 800
sc_height = 500
pl_st_x = 370
pl_st_y = 300
en_st_y_min = 50
en_st_y_max = 150
en_sp_x = 4
en_sp_y = 40
bul_sp_y = 10
coll_dis = 27

pygame.init()
screen = pygame.display.set_mode((sc_wid,sc_height))
bg = pygame.image.load('bg.jpg')
pygame.display.set_caption("space invader")
playerimg = pygame.image.load('rocket.png')
player_x = pl_st_x
player_y = pl_st_y
player_x_change = 0
e_img = []
e_x = []
e_y = []
e_x_change = []
e_y_change = []
numofenemies = 3
for i in range(numofenemies):
    e_img.append(pygame.image.load('enamy.png'))
    e_x.append(random.randint(0,sc_wid -64))
    e_y . append(random.randint(en_st_y_min, en_st_y_max))
    e_x_change.append(en_sp_x)
    e_y_change.append(en_sp_y)
bulletimg =   pygame.image.load('bullet.png')
bx = 0
by = pl_st_y
by_change = bul_sp_y
bullet_state = 'ready'
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
ty = 10
tx = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x,y):
    score =  font.render("score : " + str(score_value),True,(255,255,255))
    screen.blit(score(x,y))
def game_over_text()    :
    over_text = over_font.render("game over you lost sillygoose", True,(255,57,67))
    screen.blit(over_text,28,254)
def player(x,y)    :
    screen.blit(playerimg,(x,y))
def enemy(x,y,i)    :
        screen.blit(e_img[i],(x,y))
def fire_bullet(x,y)        :
     global bullet_state
     bullet_state = "fire"
     screen.blit(bulletimg,(x + 16 , y+ 10))
def iscollision(e_x,e_y,bx,by) :
     distance = math.sqrt((e_x - bx)**2 + (e_y - by)**2 )  
     return distance < coll_dis
running = True
while running:
     screen.fill((0,0,0))  
     screen.blit(bg, (0,0))
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
               running = False
        if event.type == pygame.KEYDOWN:      
            if event.key == pygame.K_LEFT:
                   player_x_change = -5
            if event.key == pygame.K_RIGHT:
                   player_x_change = 5
            if event.key == pygame.K_SPACE  and bullet_state == 'ready':
                 bx = player_x
                 fire_bullet(bx,by)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]   :
             player_x_change = 0
    player_x += player_x_change


            
