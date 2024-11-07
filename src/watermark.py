from PIL import Image, ImageChops
import random

def main():
    with (Image.open('img//RetroComputer_IJustGoByRay.png') as img,
          Image.open('watermark(s)//IJustGoByRay_LOGO_C.png') as wm):
        resized_wm = wm.resize((wm.width//2, wm.height//2))
        multiply_wm = ImageChops.multiply(img, resized_wm)
        x = random.randrange(10, (img.width-resized_wm.width))
        y = random.randrange(10, (img.height-resized_wm.height))
        img.paste(multiply_wm, (x, y), mask=multiply_wm.getchannel('A'))
        img.show()

if __name__ == "__main__":
    main()