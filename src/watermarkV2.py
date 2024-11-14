import pygame

class Shape():
    def __init__(self, surface, color, pos, size):
        self.surface = surface
        self.pos = pos
        self.size = size
        self.color = color


def main():
    pygame.init()
    pygame.display.set_caption("WaterMarker")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color(30, 30, 30, 255))
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()