# import pygame
# pygame.init()
# window = pygame.display.set_mode((400 , 400))
# window.fill(("black"))
# GREEN = (0 , 255 , 0)
# pygame.draw.circle(window, GREEN,(300,300),50)
# pygame.draw.circle(window, GREEN,(100,100),50,3)
# pygame.draw.rect(window,(154,62,82),pygame.Rect(200,30,80,80))
# pygame.display.update()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT    :
#             running = False
# pygame.quit()

import pygame
pygame.init()
display = pygame.display.set_mode((300,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            print("A KEY IS PRESSED")     