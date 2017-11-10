# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:36:15 2017

@author: 雨成天01
"""

background_image_filename = "C:/Users/ppsair/Desktop/python.PNG"
sprite_image_filename = "C:/Users/ppsair/Desktop/pythoncanon1.PNG"
small_fire_image_filename = "C:/Users/ppsair/Desktop/smallfire.PNG"
people_image_filename = "C:/Users/ppsair/Desktop/people.PNG"
information="your score : "

import pygame
from pygame.locals import*
from sys import exit
import pygame as py
import math

pygame.init()
 
screen = pygame.display.set_mode((815,450), 0, 32)

background = pygame.image.load(background_image_filename)
sprite = pygame.image.load(sprite_image_filename)
smallfire = pygame.image.load(small_fire_image_filename)
people = pygame.image.load(people_image_filename)


delt_t =  0.5
B = 0.00004 
g = 9.8
h = 2.5
a = 0.0065
T_ref = 300
T = 300
angel = 0



while True:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    screen.blit(background,(0,0))
    screen.blit(sprite,(0,350))
    screen.blit(people,(500,320))  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                angel += 1
            elif event.key == pygame.K_DOWN:
                angel += -1                
            elif event.key == pygame.K_SPACE:
                v = 700
                v_x = v*math.cos(math.radians(angel))
                v_y = v*math.sin(math.radians(angel))
                x = 0
                y = 0
                while True:
                    x = x + v_x*delt_t
                    y = y + v_y*delt_t
                    p=(1-a*y/T)*(T/T_ref)
                    B_cor = B*math.pow(p,h)
                    v_x = v_x - B_cor*v*v_x*delt_t
                    v_y = v_y - g*delt_t - B_cor*v*v_y*delt_t
                    v = math.sqrt(v_x*v_x + v_y*v_y)
                    
                   
                    if y > 0:
                        pygame.draw.circle(screen,(23,23,23),(int(x/30000*800),int(450-(y/10000*300))),5,5)
                        pygame.display.update()
                    else:
                        score_percentage = int(abs((x/30000*800))/550*100)
                        score = str(score_percentage)
                        score = information+score
                        my_font=pygame.font.SysFont("arial",40)
                        name_surface=my_font.render(score,True,(0,0,0),(255,255,255))
                        show_angel=pygame.font.SysFont("arial",40)
                        angel_show=show_angel.render("angle :"+str(angel),True,(0,0,0),(255,255,255))
                        screen.blit(angel_show,(500,0))
                        screen.blit(name_surface,(0,0))
                        screen.blit(smallfire,(x/30000*800,300))
                        break
    
        pygame.display.update()      
    