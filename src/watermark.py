from PIL import Image

def main():
    with (Image.open('img//sample_img.png') as img,
          Image.open('watermark(s)//sample_watermark.png') as wm):
        img.paste(wm, (500, 500), mask=wm.getchannel('A'))
        img.show()

if __name__ == "__main__":
    main()