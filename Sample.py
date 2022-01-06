import pygame as pg

class Sample:
    def __init__(self, path) -> None:
        self.path = path

    def loadSample(self):
        pg.mixer.Sound(self.path)

    