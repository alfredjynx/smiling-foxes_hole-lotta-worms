import random
import numpy as np

class Planeta:
    def __init__(self,pos,forca):
        self.__forca = forca
        self.__pos = pos

    def calcula_a(self,s):
        C = self.__forca
        y = self.__pos - s
        d = np.linalg.norm(y)
        direcao_a = y /d
        mag_a = C / d**2
        a = direcao_a * mag_a
        return a
    
    def randomized(self,x1,x2,y1,y2):
        self.__forca = random.randint(200,400)
        self.__pos = np.array([random.randint(x1,x2),random.randint(y1,y2)])

    def get_pos(self): return self.__pos
    def get_forca(self): return self.__forca

    def set_forca(self,forca):
        self.__forca = forca