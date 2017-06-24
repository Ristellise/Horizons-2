import pygame


class bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = 10
        self.w = 10
        self.rect = pygame.Rect(self.x, self.y, self.h, self.w)

    def draw(self, canvas):
        pygame.draw.rect(canvas, (0, 255, 0), (self.x, self.y, self.w, self.h))

    def overlaps(self, otherrect):
        return otherrect.colliderect(pygame.Rect(self.x, self.y, self.h, self.w))


class enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = 10
        self.w = 10
        self.rect = pygame.Rect(self.x, self.y, self.h, self.w)

    def draw(self, canvas):
        pygame.draw.rect(canvas, (0, 255, 0), (self.x, self.y, self.w, self.h))

    def overlaps(self, otherrect):
        return otherrect.colliderect(pygame.Rect(self.x, self.y, self.h, self.w))
