import pygame
from tkinter import filedialog
from PIL import Image
import random

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

def gui_init(art):
    # for opening image button
    art.define_shape(pos=(100, 100), size=(100, 50), color=(255, 0, 0), function="open_img")
    art.define_text(pos=(100, 100), size=50, text="IMG")
    # for opening watermark button
    art.define_shape(pos=(300, 100), size=(100, 50), color=(255, 0, 0), function="open_wm")
    art.define_text(pos=(300, 100), size=50, text="WM")
    # for saving image button
    art.define_shape(pos=(300, 300), size=(100, 50), color=(255, 0, 0), function="save")
    art.define_text(pos=(300, 300), size=50, text="Save")

def open_img(press):
    file_path = filedialog.askopenfilename()
    return file_path

def open_wm(press):
    file_path = filedialog.askopenfilename()
    return file_path

def save(image, watermark):
    filepath = filedialog.askdirectory()
    with (Image.open(f"r{image}") as img,
          Image.open(f"r{watermark}") as wm):
        resized_wm = wm.resize((wm.width//2, wm.height//2))
        new_img = Image.new('RGBA', size=(img.width, img.height), color=(255, 255, 255, 0))
        x = random.randrange(5, (new_img.width-resized_wm.width))
        y = random.randrange(5, (new_img.height-resized_wm.height))
        new_img.paste(resized_wm, (x, y), mask=resized_wm.getchannel('A'))
        img.paste(new_img, (0,0), mask=new_img.getchannel('A'))
        img.save(filepath+"/test.png")

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
                if function == "open_img":
                    img = exec(f"{function}" + "(None)")
                if function == "open_wm":
                    wm = exec(f"{function}" + "(None)")
                if function == "save":
                    exec(f"{function}({img},{wm})")
        screen.fill(pygame.Color(30, 30, 30, 255))
        art = UI(screen)
        gui_init(art)
        art.draw()
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()