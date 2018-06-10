import sys
import pygame
import time
import random

import settings as C
from snake import Snake


class SnakeGame:
    def __init__(self):
        self.wall = []
        self.apple = ()
        pygame.init()
        self.screen = pygame.display.set_mode(C.RES)
        self.snake = Snake(self.screen)
        pygame.display.set_caption(C.WINDOW_CAPTION)

    def generate_walls(self):
        for n in range(20, C.RES[0], 20):
            pygame.draw.circle(self.screen, (0, 0, 255), (n, 20), 10)
            self.wall.append([n, 20])
            pygame.draw.circle(self.screen, (0, 0, 255), (n, C.RES[1] - 20), 10)
            self.wall.append([n, C.RES[1] - 20])
        for n in range(20, C.RES[1], 20):
            pygame.draw.circle(self.screen, (0, 0, 255), (20, n), 10)
            self.wall.append([20, n])
            pygame.draw.circle(self.screen, (0, 0, 255), (C.RES[0] - 20, n), 10)
            self.wall.append([C.RES[0] - 20, n])
        pygame.display.flip()

    def create_apple(self):
        self.apple = ()
        while (list(self.apple) in self.wall) or (list(self.apple) in self.snake.elements) or (not self.apple):
            self.apple = (random.randrange(40, C.RES[0] - 40, 20),
                          (random.randrange(40, C.RES[1] - 40, 20)))

        pygame.draw.circle(self.screen, (255, 0, 0), self.apple, C.RADIUS)
        pygame.display.flip()

    def event_loop(self):
        while True:
            time.sleep(C.WAIT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_DOWN) and \
                            (self.snake.speed != [0, -2 * C.RADIUS]):
                        self.snake.speed = [0, 2 * C.RADIUS]
                    elif (event.key == pygame.K_UP) and \
                            (self.snake.speed != [0, 2 * C.RADIUS]):
                        self.snake.speed = [0, -2 * C.RADIUS]
                    elif (event.key == pygame.K_RIGHT) and \
                            (self.snake.speed != [-2 * C.RADIUS, 0]):
                        self.snake.speed = [2 * C.RADIUS, 0]
                    elif (event.key == pygame.K_LEFT) and \
                            (self.snake.speed != [2 * C.RADIUS, 0]):
                        self.snake.speed = [-2 * C.RADIUS, 0]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            self.snake.move(cbk_dead=self.check_dead,
                            cbk_apple=self.check_apple)

    def exit_dead(self):
        print("Difficulty:\t%d" % C.DIFFICULTY)
        print("Bugs eaten:\t%d" % (len(self.snake.elements) - C.START_LENGTH + 1))
        print("Score:\t\t%d" % ((len(self.snake.elements) - C.START_LENGTH + 1) * C.DIFFICULTY))
        time.sleep(1)
        self.exit_game()

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def check_dead(self):
        """check_dead function
        """
        if list(self.snake.get_head()) in self.snake.elements[1:]:
            self.exit_dead()
        if list(self.snake.get_head()) in self.wall:
            self.exit_dead()

    def check_apple(self):
        if self.snake.get_head() == self.apple:
            self.snake.eat()
            self.create_apple()

    def run(self):
        self.generate_walls()
        self.create_apple()
        self.event_loop()

