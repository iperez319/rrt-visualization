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

#Linked List class
class Node():
    def __init__(self,location,parent,cost):
        self.location = location
        self.parent= parent
        self.cost = cost

#Class for the rectangular boundaries in the map
class Boundaries():
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

#RRT Graph Class
class RRT_Star():
    def __init__(self,start,end,min_length,max_length,node_number,boundaries,r):
        self.start= Node(start, None,0) 
        self.end=end
        self.min_length = min_length #min length between 2 nodes
        self.max_length=max_length #max lengh between 2 nodes
        self.node_number = node_number #max number of nodes in a tree
        self.screen_size=(800,800) #size of the popup screen (pygame)
        self.color = (255,255,0) #endpoint color
        self.color1 = (0,0,255) #startpoint color
        self.colorRect= (255,0,255) #color of the rectangular buondaries 
        self.radius = 10 #radius of the circle surrounding the startpoint and the endpoint
        self.nodes = [] #list of the Nodes()
        self.nodes.append(self.start) #adds the starting node into the Node list
        self.boundaries = boundaries 
        #self.node_dict = {start:0} #dictionary containing the ndoes and their "cost, or distance from the startpoint"
        self.r = r #radius of the circle for RRT*
        self.shortest = float('inf')
    
    def dist(self,p1,p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

    def find_closest(self, p1):
        closest = self.nodes[0]
        for node in self.nodes:
            if self.dist(node.location,p1) < self.dist(closest.location,p1):
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

        if self.dist(closest.location,nn) > self.max_length:
            length = self.dist(closest.location,nn)
            x = closest.location[0]+int(self.max_length*(x-closest.location[0])/length)
            y = closest.location[1]+int(self.max_length*(y-closest.location[1])/length)   
            nn=(x,y)

        closest = self.find_closest(nn)

        if self.dist(closest.location,nn) < self.min_length:
            length = self.dist(closest.location,nn)
            while length == 0:
                nn = self.new_node()
            x = closest.location[0]+int(self.min_length*(x-closest.location[0])/length)
            y = closest.location[1]+int(self.min_length*(y-closest.location[1])/length)

        if not self.isValid(nn):
            closest,nn = self.new_node()

        return closest,nn

    def find_cheapest(self, p1):
        close_nodes=[]
        for node in self.nodes:
            if self.dist(node.location,p1) <= self.r:
                close_nodes.append(node)

        cheapest = close_nodes[0]
        for node in close_nodes:
            if (self.dist(node.location,p1) + node.cost) < (self.dist(cheapest.location, p1) + cheapest.cost):
                cheapest = node 
        return cheapest

    def rewire(self,new_node):
        close_nodes=[]
        for node in self.nodes:
            if self.dist(node.location,new_node.location) <= self.r:
                close_nodes.append(node)
        for node in close_nodes:
            if (node.cost > new_node.cost+ self.dist(new_node.location,node.location)):
                node.parent = new_node

    def main(self):
    
        pygame.init()
        
        #sets screen size
        screen = pygame.display.set_mode(self.screen_size)
        
        #sets the title of the screen
        pygame.display.set_caption("RRT* Algorithm")

        #filles the screen with the color white
        white = (255,255,255)
        screen.fill(white)
        
        #draws a circle around the startpoint
        pygame.draw.circle(screen,self.color1,self.start.location,self.radius)

        #draws a circle around the endpoint
        pygame.draw.circle(screen, self.color, self.end, 5*self.radius)

        for i in self.boundaries:
            pygame.draw.rect(screen,self.colorRect,pygame.Rect(i.x1,i.y1,abs(i.x2-i.x1),abs(i.y2-i.y1)))

        current = self.start

        for n in range(self.node_number):

            closest, nn = self.new_node() #returns a valid new node and the closest node to it
            cheapest = self.find_cheapest(nn)

            recent=Node(nn, cheapest, cheapest.cost+self.dist(nn,cheapest.location))
            self.nodes.append(recent)

            self.rewire(recent)
         

            red = (255,0,0)
            pygame.draw.circle(screen,red,nn,3)
            pygame.draw.line(screen,red,cheapest.location,nn,2)

            #green = (0,255,0)
            #pygame.draw.line(screen,green,nn,closest.location,2)

            #updates the screen when you add a new node
            pygame.display.update()

            if (self.dist(nn,self.end) <= 5*self.radius) and recent.cost < self.shortest:

                print("DONE")
                print(recent.cost)
                self.shortest = recent.cost

                while current != self.start:
                    pygame.draw.line(screen,(255,0,0),current.parent.location,current.location,2)
                    current = current.parent

                current = recent
                while current != self.start:
                    pygame.draw.line(screen,(0,255,0),current.parent.location,current.location,2)
                    current = current.parent


                pygame.display.update()
                 

            if (pygame.event.poll().type == pygame.QUIT):
                break
        while True:
            # gets a single event from the event queue
            event = pygame.event.poll()

            # if the 'close' button of the window is pressed
            if event.type == pygame.QUIT:
                # stops the application

                #print(self.node_dict)
                break
            
if __name__ == '__main__':
    boundaries = [Boundaries(100,100,200,200), Boundaries(101,202,303,404)]
    RRT_Star((375,375),(600,600),5,20,500,boundaries,30).main()
