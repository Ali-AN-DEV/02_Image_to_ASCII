import argparse
import numpy as np
from PIL import Image

# 70 levels of gray (FIXED TO 70 CHARACTERS)
gscale1 = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 levels of gray
gscale2 = "@%#*+=-:. "

def getAverageL(image):
    im = np.array(image)
    w, h = im.shape
    return np.average(im.reshape(w * h))

def convertImageToAscii(fileName, cols, scale, moreLevels):
    global gscale1, gscale2

    image = Image.open(fileName).convert('L')
    W, H = image.size
    print(f"Input image dimensions: {W} x {H}")

    w = W / cols
    h = w / scale
    rows = int(H / h)

    print(f"cols: {cols}, rows: {rows}")
    print(f"tile dimensions: {w:.2f} x {h:.2f}")

    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    aimg = []
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        if j == rows - 1:
            y2 = H
        aimg.append("")
        for i in range(cols):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == cols - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageL(img))
            # Clamp index to valid range (0-69)
            idx = min(int((avg * 69) / 255), 69)
            gsval = gscale1[idx] if moreLevels else gscale2[int((avg * 9) / 255)]
            aimg[j] += gsval
    return aimg

def main():
    parser = argparse.ArgumentParser(description="Convert image to ASCII art.")
    parser.add_argument("--file", dest="imgFile", required=True, help="Input image file")
    parser.add_argument("--cols", dest="cols", type=int, help="Number of columns")
    parser.add_argument("--scale", dest="scale", type=float, default=0.43, help="Scale factor")
    parser.add_argument("--more", dest="moreLevels", action="store_true", help="Use 70 levels scale")
    args = parser.parse_args()

    if not args.cols:
        args.cols = 80

    ascii_art = convertImageToAscii(args.imgFile, args.cols, args.scale, args.moreLevels)
    print("\n".join(ascii_art))

if __name__ == "__main__":
    main()