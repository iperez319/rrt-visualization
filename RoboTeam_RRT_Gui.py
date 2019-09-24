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

class RRT():
    def __init__(self,start,end,min_length,max_length,node_number):
        self.start= start
        self.end=end
        self.min_length = min_length
        self.max_length=max_length
        self.node_number = node_number
        self.screen_size=(800,800)
        self.color = (0,0,0)
        self.radius = 20
        self.nodes = []
        self.nodes.append(start)
        self.node_pairs=[]
    
    def dist(self,p1,p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

    def find_closest(self, p1):
        closest = self.nodes[0]
        for node in self.nodes:
            if self.dist(node,p1) < self.dist(closest,p1):
                closest = node
        return closest

    def new_node(self):
        x = int(random.randint(0,self.screen_size[0]+1))
        y= int(random.randint(0,self.screen_size[1]+1))
        nn=(x,y)
        closest = self.find_closest(nn)

        if self.dist(closest,nn) > self.max_length:
            length = self.dist(closest,nn)
            x = closest[0]+int(self.max_length*(x-closest[0])/length)
            y = closest[1]+int(self.max_length*(y-closest[1])/length)   

            """
            angle = math.atan((nn[1]-closest[1])/(nn[0]-closest[0]))
            x=int(closest[0]+self.max_length*math.cos(angle))
            y = int(closest[1]+self.max_length*math.sin(angle))
            print(x,y)
            print()
            """
            nn=(x,y)

        closest = self.find_closest(nn)

        if self.dist(closest,nn) < self.min_length:
            length = self.dist(closest,nn)
            if length == 0:
                nn = self.new(node)
            x = closest[0]+int(self.min_length*(x-closest[0])/length)
            y = closest[1]+int(self.min_length*(y-closest[1])/length)
            """
            angle = math.atan((nn[1]-closest[1])/(nn[0]-closest[0]))
            x=int(closest[0]+self.min_length*math.cos(angle))
            y = int(closest[1]+self.min_length*math.sin(angle))
            nn=(x,y)
            """

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
        pygame.draw.circle(screen,self.color,self.start,self.radius)

        #draws a circle around the endpoint
        pygame.draw.circle(screen, self.color, self.end, self.radius)

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

            blue = (0,0,255)
            pygame.draw.circle(screen,blue,nn,3)
            pygame.draw.line(screen,blue,cl,nn,2)
            #updates the screen when you add a new node
            pygame.display.update()
        
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
    RRT((375,375),(750,750),10,50,500).main()


"""
start=(1,1)
end=(50,50)

verts = [start]
codes=[Path.MOVETO]
stem_length = 5

previous = start

for i in range(5):
	x = random.randint(-10,10+1)
	y = random.randint(-10,10+1)
	if (math.sqrt((x-previous[0])**2+(y-previous[1])**2) > stem_length):
		x /=math.sqrt((x-previous[0])**2+(y-previous[1])**2)
		y /= math.sqrt((x-previous[0])**2+(y-previous[1])**2)
	#y_limit = int(math.sqrt(stem_length**2-x**2))
	#y = random.randint(-y_limit,y_limit)
	point=(x,y)
	verts=[start,point]
	codes=[Path.MOVETO,Path.LINETO]

	path=Path(verts,codes)

	fig,ax = plt.subplots()
	patch = patches.PathPatch(path)
	ax.add_patch(patch)
	ax.set_xlim(-10,10)
	ax.set_ylim(-10,10)
	plt.show()
	print(point)
	previous = point
"""