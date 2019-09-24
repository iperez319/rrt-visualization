#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:48:16 2019

@author: zoe
"""
"""
#import matplotlib
from tkinter import *


main=Tk()
main.title('RoboTeam_RRT_GUI') #renames the title of the main window

mainFrame= Frame(main) 
mainFrame.pack()

"""
import numpy as np
import random, math
import pygame.locals
import pygame.draw
#import matplotlib.pyplot as plt
#from matplotlib.path import Path 
#import matplotlib.patches as patches

class Boundaries():
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class RRT():
    def __init__(self,start,end,min_length,max_length,node_number,boundaries):
        self.start= start
        self.end=end
        self.min_length = min_length
        self.max_length=max_length
        self.node_number = node_number
        self.screen_size=(800,800)
        self.color = (255,255,0)
        self.color1 = (0,0,255)
        self.colorRect= (255,0,255)
        self.radius = 20
        self.nodes = []
        self.nodes.append(start)
        self.node_pairs=[]
        self.boundaries = boundaries
    
    def dist(self,p1,p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

    def find_closest(self, p1):
        closest = self.nodes[0]
        for node in self.nodes:
            if self.dist(node,p1) < self.dist(closest,p1):
                closest = node
        return closest

    def isValid(self,p1):
        for i in self.boundaries:
            if (p1[0] > i.x1 and p1[0] < i.x2) and (p1[1] > i.y1 and p1[1] < i.y2):
                return False
        return True

    def new_node(self):
        x = int(random.randint(0,self.screen_size[0]+1))
        y= int(random.randint(0,self.screen_size[1]+1))
        nn=(x,y)
        closest = self.find_closest(nn)

        if self.dist(closest,nn) > self.max_length:
            length = self.dist(closest,nn)
            x = closest[0]+int(self.max_length*(x-closest[0])/length)
            y = closest[1]+int(self.max_length*(y-closest[1])/length)   
            nn=(x,y)

        closest = self.find_closest(nn)

        if self.dist(closest,nn) < self.min_length:
            length = self.dist(closest,nn)
            if length == 0:
                nn = self.new(node)
            x = closest[0]+int(self.min_length*(x-closest[0])/length)
            y = closest[1]+int(self.min_length*(y-closest[1])/length)

        if not self.isValid(nn):
            closest,nn = self.new_node()

        return closest,nn

    def main(self):
    
        pygame.init()
        
        #sets screen size
        screen = pygame.display.set_mode(self.screen_size)
        
        #sets the title of the screen
        pygame.display.set_caption("RRT Algorithm")

        #filles the screen with the color white
        white = (255,255,255)
        screen.fill(white)
        
        #draws a circle around the startpoint
        pygame.draw.circle(screen,self.color1,self.start,self.radius)

        #draws a circle around the endpoint
        pygame.draw.circle(screen, self.color, self.end, self.radius)

        for i in self.boundaries:
            pygame.draw.rect(screen,self.colorRect,pygame.Rect(i.x1,i.y1,abs(i.x2-i.x1),abs(i.y2-i.y1)))

        #pygame.draw.rect(screen,self.colorRect,)

        for n in range(self.node_number):

            cl, nn = self.new_node()

            """
            x = int(random.randint(0,480+1))
            y= int(random.randint(0,640+1))
            nn=(x,y)

            closest = self.find_closest(nn)

            if self.dist(closest,nn) > self.max_length:
                angle = math.atan((nn[1]-closest[1])/(nn[0]-closest[0]))
                x=int(closest[0]+self.max_length*math.cos(angle))
                y = int(closest[1]+self.max_length*math.sin(angle))
                nn=(x,y)

            closest = self.find_closest(nn)
            """

             
            self.nodes.append(nn)
            self.node_pairs.append((cl,nn))

            red = (255,0,0)
            pygame.draw.circle(screen,red,nn,3)
            pygame.draw.line(screen,red,cl,nn,2)

            #updates the screen when you add a new node
            pygame.display.update()

            if (self.dist(nn,self.end) <= self.radius):
                break

            if (pygame.event.wait().type == pygame.QUIT):
                break
        while True:
            # gets a single event from the event queue
            event = pygame.event.wait()

            # if the 'close' button of the window is pressed
            if event.type == pygame.QUIT:
                # stops the application
                break
            
if __name__ == '__main__':
    boundaries = [Boundaries(100,100,200,200), Boundaries(101,202,303,404)]
    RRT((375,375),(750,750),5,20,500,boundaries).main()
