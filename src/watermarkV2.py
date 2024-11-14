import pygame
import os

class Shape():
    def __init__(self, surface, color, pos, size, function):
        self.surface = surface
        self.pos = pos
        self.size = size
        self.color = pygame.Color(color)
        self.function = function

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

class UI():
    def __init__(self, surface):
        self.surface = surface
        self.shape = []
        self.text = []

    def define_shape(self, pos, size, color, function):
        shape = Shape(surface=self.surface, pos=pos, size=size, color=color, function=function)
        self.shape.append(shape)  

    def define_text(self, text, pos, size):
        text = Text(surface=self.surface, text=text, pos=pos, size=size)
        self.text.append(text)  

    def draw(self):
        for shape in self.shape:
            shape.draw()
        for text in self.text:
            text.draw()

    def button(self, pos):
        for shape in self.shape:
            if shape.function != None:
                if (shape.pos[0] < pos[0] and (shape.pos[0] + shape.size[0]) > pos[0] and 
                    shape.pos[1] < pos[1] and (shape.pos[1] + shape.size[1]) > pos[1]):
                    return shape.function
            return None

def gui_init(art):
    art.define_shape(pos=(100, 100), size=(50, 50), color=(255, 0, 0), function="test")

def test(press):
    print("pressed")

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                function = art.button(pygame.mouse.get_pos())
                if function != None:
                    exec(f"{function}" + "(None)")
        screen.fill(pygame.Color(30, 30, 30, 255))
        art = UI(screen)
        gui_init(art)
        art.draw()
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()