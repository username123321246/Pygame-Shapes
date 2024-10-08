import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
color = (5,60,230)


class Circle():
    def __init__(self, color, pos, radius, width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_surface = screen

    def draw(self):
        self.draw_Circle = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

    def grow(self,r):
        self.circle_radius = self.circle_radius + r
        self.draw_Circle = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

# making instance
circle2 = Circle(color, (300,300), 25, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            circle2.draw()
            pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            circle2.grow(25)
            pygame.display.update()
























