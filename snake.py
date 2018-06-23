import pygame
import settings as C


class Snake:
    def __init__(self, screen):
        self.headx = 100
        self.heady = 100
        self.length = C.START_LENGTH
        self.elements = [[self.headx, self.heady]]

        while len(self.elements) != (self.length - 1):
            self.elements.append([self.headx, self.heady])
        self.speed = [C.RADIUS * 2, 0]
        self.screen = screen
        pygame.draw.circle(self.screen, (255, 255, 0), (self.headx, self.heady),
                           C.RADIUS)
        pygame.display.flip()

    def move(self, cbk_dead, cbk_apple):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.elements[-1][0],
                                                    self.elements[-1][1]), C.RADIUS)
        self.elements.pop()
        self.headx += self.speed[0]
        self.heady += self.speed[1]
        self.elements = [[self.headx, self.heady]] + self.elements[0:]
        cbk_dead()
        for element in self.elements[1:]:
            pygame.draw.circle(self.screen, (255, 255, 0), (element[0], element[1]),
                               C.RADIUS)
        pygame.draw.circle(self.screen, (0, 255, 0), (self.headx, self.heady),
                           C.RADIUS)
        pygame.display.flip()
        cbk_apple()

    def eat(self):
        self.elements.append(self.elements[-1])

    def get_head(self):
        return self.headx, self.heady
