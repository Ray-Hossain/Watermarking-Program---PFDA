import pygame

class Shape():
    def __init__(self, surface, color, pos, size):
        self.surface = surface
        self.pos = pos
        self.size = size
        self.color = pygame.Color(color)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, ((self.pos), (self.size)))

class Text():
    def __init__(self, surface, text, pos, size):
        self.surface = surface
        self.pos = pos
        self.size = size
        self.text = text

    def draw(self):
        font = pygame.font.SysFont("arial", self.size)
        text = font.render(self.text, True, "White")
        self.surface.blit(text, self.pos)

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
        button = Shape(surface=screen, color=(255, 0, 0), pos=(200, 200), size=(50, 50))
        text = Text(surface=screen, text="Open", pos=(200,200), size=30)
        button.draw()
        text.draw()
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()