from PIL import Image
from sys import argv

IMG, OUTPUT = argv[1:3]

def get_char(r,g,b,alpha=255):
    if alpha == 0:
        return ' '
#    else:
    char_list = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\^`'.")
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    unit = (255 + 1.0)/69
    return char_list[int(gray/unit)]

if __name__ == '__main__':
    raw_image = Image.open(IMG)
    image = raw_image.convert('RGBA')
    img = image.resize((80,80))
    text = ""
    width, height = img.size
    for i in range(height):
        for j in range(width):
            text += get_char(*img.getpixel((j,i)))
        text += "\n"

    print(text)

    with open(OUTPUT, 'w') as f:
        f.write(text)
