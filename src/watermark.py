from PIL import Image, ImageChops
import random

def main():
    with (Image.open('img//RetroComputer_IJustGoByRay.png') as img,
          Image.open('watermark(s)//IJustGoByRay_LOGO_C.png') as wm):
        resized_wm = wm.resize((wm.width//2, wm.height//2))
        new_img = Image.new('RGBA', size=(img.width, img.height), color=(255, 255, 255, 0))
        # multiply_wm = ImageChops.multiply(img, resized_wm)
        x = random.randrange(5, (new_img.width-resized_wm.width))
        y = random.randrange(5, (new_img.height-resized_wm.height))
        new_img.paste(resized_wm, (x, y), mask=resized_wm.getchannel('A'))
        opacity = 0.5
        new_img.putalpha(int(255 * opacity))
        img.paste(new_img, (0, 0), new_img)
        # img.paste(new_img, (0,0), mask=new_img.getchannel('A'))
        img.show()
        

if __name__ == "__main__":
    main()