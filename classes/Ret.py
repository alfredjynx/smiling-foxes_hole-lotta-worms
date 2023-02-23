import random
import numpy as np
import pygame

class Ret:

    def __init__(self,pos,tam):
        self.__pos = pos
        self.__rect = pygame.Rect(pos,tam)
    
    def getPos(self):
        return self.__pos
    
    def setPos(self, pos):
        self.__pos  = pos

    def getRect(self):
        return self.__rect
    
    def setRect(self, rect:pygame.Rect):
        self.__rect = rect
    
    def setTamanho(self,tam):
        self.__rect = pygame.Rect(self.__pos,tam)

    def collide(self,p):
        return self.__rect.collidepoint(p)


    
