# Watermark-er

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <https://github.com/Ray-Hossain/Watermarking-Program---PFDA>

## Description
The Watermark-er is a program for artists to be able to watermark or sign their own images without needing a drawing or photo editing program to do it. Place your images that you wished to be watermarked in the "img" folder, your personal watermark in the "wm" folder, and then export your final image in the "export" folder. When running the program, a menu with 3 buttons will be displayed. The "Image" button opens your file explorer so that you can select the image you want watermarked. The "Watermark" button will do the same thing, but still time you will have to select your watermark. The "Save" Button will allow you to save the image. You may select the "export" folder as the directory you want to say have, but you can also choose another place to save your images to.

What the program is doing internally is that when given the image and watermark, it will place the watermark randomly but will keep it within the confines of the length and width of the image. This will prevent the watermark from going off the edge of the image. At the same time, it is also reducing the opacity of the watermark so that it doesn't overpower your image. The only important files included within this repository are in the "src" folder, which is the watermarker.py file. This is the file that includes the code and will run the program. The other files in this repository are proposal.md, requirements.txt, sample_img.png inside the "img" folder, and sameple_watermark.png.

There is a lot of room for improvement with the current version of this program. As of right now, there isn't a way to change the opacity and size of the watermark without manually editing the code. If you wish to change these aspects, you will need to have VS Code or some sort of code editing application and a knowledge of Python in order to change the code. Another improvement is a way to see where the program randomly placed your watermark before saving it. Finally, I never found a straight forward solution to edit the metadata of the image, so I will havet to come back to this in the future. However, as of me writing this, I am quite proud of what I've accomplished. I'll probably come back and change aspects of it in the future, but this is where the Watermark-er stands right now. It may not be the most major program, but to me it was quite the undertaking, but I'm glad to have made it.