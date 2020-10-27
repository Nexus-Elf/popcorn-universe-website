import pygame
import random
import time
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
screen_width = 1200
screen_height = 600
pygame.init()
wn = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Popcorn Universe Snake Game')
run = True
x1 = 300
y1 = 300
char_size=100
food_size=100
foodx=round(random.randrange(0,1200)/10)*10
foody=round(random.randrange(0,600)/10)*10
x1_change = 0       
y1_change = 0
movement_speed=20
clock = pygame.time.Clock()
char_colors=[(50,50,50), (100,100,100), (150,150,150), (200,200,200)]
colors_index=0
score=0
best_score=0
font = pygame.font.Font('freesansbold.ttf', 30) 
grey = (100, 100, 100)
text = font.render(f'Score: {score}', True, grey)
textRect = text.get_rect()  
textRect.center = (300, 30) 
best_score_t = font.render(f'Best Score: {best_score}', True, grey)
bs_rect = best_score_t.get_rect()  
bs_rect.center = (600, 30) 
decrease_index=0
while run:
    decrease_index+=1
    if decrease_index>90:
        if int(char_size)>30 and int (food_size)>30:
            char_size/=2
            food_size/=2
            decrease_index=0
            if 0<=colors_index<len(char_colors)-1:
                colors_index+=1
            if movement_speed>10:
                movement_speed-=5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -movement_speed
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = movement_speed
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -movement_speed
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = movement_speed
                x1_change = 0
        if event.type == pygame.QUIT:
            run = False
    if 0<=x1<=1200:
        x1 += x1_change
    else:
        if x1<0:
            x1=1200    
        else:
            x1=0
    if 0<=y1<=700:
        y1 += y1_change
    else:
        if y1<0:
            y1=700
        else:
            y1=0
    wn.fill(white)
    pygame.draw.rect(wn, char_colors[colors_index], [x1, y1, char_size, char_size])   
    pygame.draw.rect(wn, (100,200,100), (foodx, foody, food_size,food_size))
    if x1==foodx and y1==foody:
        foodx=round(random.randrange(0,1200)/10)*10
        foody=round(random.randrange(0,700)/10)*10
        print("foodx: ", foodx, "foody:", foody)
        if (foodx>900 or foodx<100 or foody>500 or foody<100):
            while(foodx>900 and foodx<100 and foody>500 and foody<100):
                foodx=round(random.randrange(0,1200)/10)*10
                foody=round(random.randrange(0,700)/10)*10
        if int(char_size)<100 and int(food_size)<100:
            char_size*=2.3
            food_size*=2.3
            if 0<=colors_index<len(char_colors)-1:
                colors_index-=1
            if movement_speed>10:
                movement_speed+=4
        score+=1  
        if best_score<score:
            best_score=score
    if int(char_size)<50 or int(food_size)<50:
        score=0     
    text = font.render(f'Score: {score}', True, grey) 
    best_score_t = font.render(f'Best Score: {best_score}', True, grey)
    wn.blit(text, textRect) 
    wn.blit(best_score_t, bs_rect)
    pygame.display.update()
    clock.tick(30)
    wn.fill(black)
pygame.quit()
