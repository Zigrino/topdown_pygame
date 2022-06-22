import math
import pygame
import random
class Utils():
    def normalize_vector(self, vector):
        magnitude = float(math.sqrt(vector[0]**2 + vector[1]**2))
        if magnitude == 0:
            return (0, 0)
        return [vector[0]/magnitude, vector[1]/magnitude]
    def subtract_vectors(self, vec1, vec2):
        return (vec1[0] - vec2[0], vec1[1] - vec2[1])
        
