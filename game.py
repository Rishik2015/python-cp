# import pygame
# pygame.init

# screen = pygame.display.set_mode((800 , 600))
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill(("skyblue"))  
#     pygame.display.flip()   
# pygame.quit ()   
# 
import pygame
pygame.init()   
SCREEN_WIDTH , SCREEN_HEIHT = 500 , 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIHT))

bg_image = pygame.transform.sxale(
    pygame.image.load('images').convert(),(SCREEN_WIDTH , SCREEN_HEIHT))
batman_image = pygame .transform .scale(pygame.image.load('batman').convert_alpha(),(200,200))
batman_rect = batman_image.get_rect(center=(SCREEN_WIDTH // 2,
        SCREEN_HEIHT // 2 -50))