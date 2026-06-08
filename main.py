import pygame
import sys
from shot import Shot 
from logger  import log_event 
from asteroid import Asteroid
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroidfield  import AsteroidField 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    Player.containers = (updatable ,drawable )
    player = Player(x,y)  
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    shots = pygame.sprite.Group()
    Shot.containers = (shots,drawable,updatable)
    field = AsteroidField()
    while True :
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for d in drawable :
            d.draw(screen)
        player.draw(screen)
        updatable.update(dt)
        for obj in asteroids:
            if obj.collides_with(player) :
                  log_event("player_hit")
                  print("Game over!")
                  sys.exit()
        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot) :
                    log_event("asteroid_shot")
                    obj.split()
                    pygame.sprite.Sprite.kill(shot)
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
