import pygame
import random
from logger  import log_event 
from circleshape import CircleShape
from constants import  LINE_WIDTH,ASTEROID_MIN_RADIUS

class Asteroid(CircleShape) :
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen):
        return pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity*dt
    def split (self) :
        pygame.sprite.Sprite.kill(self)

        if self.radius < ASTEROID_MIN_RADIUS : 
             return
        log_event("asteroid_split") 
        angle = random.uniform(20,50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        r1 = self.radius -  ASTEROID_MIN_RADIUS
        r2 = self.radius -  ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x,self.position.y,r1)
        a2 = Asteroid(self.position.x,self.position.y,r2)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2
        