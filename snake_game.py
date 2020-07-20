# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:30:05 2020

@author: Lenovo
"""

import pygame
import random


pygame.init()
game_window=pygame.display.set_mode((700,500))

pygame.display.set_caption("snake game")

clock=pygame.time.Clock()



font=pygame.font.SysFont(None,50)

def print_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])
def plot_snk(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])

def gameloop():
    snk_list=[]
    snk_len=1
    velocity_x=0
    velocity_y=0
    score=0
    exit_game=False
    game_over=False
    snake_size=10
    snake_x=300
    snake_y=100
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    food_x=random.randint(0,700)
    food_y=random.randint(0,500)
    width=700
    high=500
    fps=20
    
    
    while not exit_game:
        if game_over:
            game_window.fill(white)
            print_score("Game Over",red,30,250)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-5
                        velocity_y=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=5
                        velocity_x=0
                    if event.key==pygame.K_UP:
                        velocity_y=-5
                        velocity_x=0
                    
            snake_x+=velocity_x
            snake_y+=velocity_y
            
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score=score+1
                snk_len+=5
                #print("Score:",score*10)
                food_x=random.randint(0,700)
                food_y=random.randint(0,500)
        
            
                
            game_window.fill(white)
            print_score("Score:"+str(score*10),red,10,10)
            pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_len:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
            if snake_x<0 or snake_x>width or snake_y<0 or snake_y>high:
                game_over=True
            
            #pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snk(game_window,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
            
    pygame.quit()
    quit()
    
gameloop()
