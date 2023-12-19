import pygame
import random
pygame.init()
 
blue = [230,230,250]
white  = [255, 255, 255]
size = [500, 500]
    
     
 
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Płatki śniegu")
 
snowFall = []
for i in range(30):
    x = random.randrange(0, 500)
    y = random.randrange(-400, 200)
    snowFall.append([x, y])
 
clock = pygame.time.Clock()
done = False
end = False
while not done:
 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True
    screen.fill(blue)
    
    if not end:
        for i in range(30):
            pygame.draw.circle(screen, white, snowFall[i], 15)
    
            snowFall[i][1] += 1
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if((snowFall[i][0]-15 < pos[0] and snowFall[i][0]+15 > pos[0]) and (snowFall[i][1]-15 < pos[1] and snowFall[i][1]+15 > pos[1])):
                    y = random.randrange(-50, -10)
                    snowFall[i][1] = y
                
                    x = random.randrange(0, 500)
                    snowFall[i][0] = x
                
                    
            if snowFall[i][1] >= 500:
                del snowFall
                end = True
                break
    if end:        
        pygame.font.init() 
        my_font = pygame.font.SysFont('Arial', 60)
        text_surface = my_font.render('Koniec gry', False, (0, 0, 0))
        screen.blit(text_surface, (100,250))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()