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
numofenemies = 6
for i in range(numofenemies):
    e_img.append(pygame.image.load('enamy.png'))
    e_x.append(random.randint(0,sc_wid -64))
    e_y . append(random.randint(en_st_y_min, en_st_y_max))
    e_x_change.append(en_sp_x)
    e_y_change.append(en_sp_y)
