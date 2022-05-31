import pygame, math

pygame.init()
screen = pygame.display.set_mode((1200, 600))

clock = pygame.time.Clock()

class planet:
    def __init__(self, screen, color, x, y, radius, mass):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.velx = 0
        self.vely = -100
        self.Time = 60

    def update(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def calculate_attraction(self, p):
        G = 1
        r = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
        print(r)
        Force = G * self.mass * p.mass/r**2
        s = p.x - self.x
        a = math.acos(s/r)
        Forcex = Force * math.cos(a)
        Forcey = Force * math.sin(a)
        return Forcex, Forcex

    def calculate_force(self, planets):
        totalforcex = 0
        totalforcey = 0
        for p in planets:
            self.calculate_attraction(p)

        self.velx = totalforcex / self.mass * self.Time
        self.vely = totalforcey / self.mass * self.Time


planet1 = planet(screen, (255, 255, 255), 200, 250, 10, 500)
planet2 = planet(screen, (255, 0, 0), 600, 300, 10, 100)
planets = [planet1, planet2]

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for planet in planets:
        planet.calculate_force(planets)
        planet.update()

    pygame.display.update()
    clock.tick(120)
