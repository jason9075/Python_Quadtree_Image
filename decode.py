import cv2
import math
import numpy as np
import argparse


argparser = argparse.ArgumentParser()
argparser.add_argument("image", help="path to image")
argparser.add_argument("-o", "--output", default="decode.jpg", help="output file name")

args = vars(argparser.parse_args())


def main():
    img = np.zeros((1, 1, 3), dtype=np.uint8)  # dummy
    width = 1
    height = 1

    with open(args["image"], "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            if idx == 0:
                height, width = map(int, line.split())
                img = np.zeros((height, width, 3), dtype=np.uint8)
            else:
                x, y, depth, b, g, r = map(int, line.split())
                w = int(width * math.pow(0.5, depth))
                h = int(height * math.pow(0.5, depth))
                cv2.rectangle(img, (x, y), (x + w, y + h), (b, g, r), cv2.FILLED)

    cv2.imwrite(args["output"], img)


if __name__ == "__main__":
    main()
