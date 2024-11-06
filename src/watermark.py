from PIL import Image
import random

def main():
    with (Image.open('img//sample_img.png') as img,
          Image.open('watermark(s)//sample_watermark.png') as wm):
        x = random.randrange(10, (img.width-wm.width))
        y = random.randrange(10, (img.height-wm.height))
        img.paste(wm, (x, y), mask=wm.getchannel('A'))
        img.show()

if __name__ == "__main__":
    main()