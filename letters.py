# Write your code here :-)
import pygame
import random


class Letter():
    def __init__(self, x, y):
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def letter():
    letter = alphabet[random.randint(0,25)]
    return letter

