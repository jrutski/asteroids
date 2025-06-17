import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            split_vector_1 = self.velocity.rotate(split_angle)
            split_vector_2 = self.velocity.rotate(-split_angle)

            split_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid.velocity = split_vector_1 * 1.1

            asteroid = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid.velocity = split_vector_2 * 1.1
