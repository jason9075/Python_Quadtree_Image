from main import QuadTree, get_max_depth
import cv2
import os
import argparse


argparser = argparse.ArgumentParser()
argparser.add_argument("image", help="path to image")
argparser.add_argument(
    "-t", "--threshold", default=30, help="threshold for color difference"
)
argparser.add_argument("-d", "--depth", default=8, help="max depth of quadtree")
argparser.add_argument("-e", "--encode", default="encoded.txt", help="encode to file")

args = vars(argparser.parse_args())


class ExportTree(QuadTree):
    def write(self, file):
        if self.color is not None:
            info = [
                self.boundary[0],
                self.boundary[1],
                self.depth,
                self.color[0],
                self.color[1],
                self.color[2],
            ]
            file.write(" ".join(map(str, info)) + "\n")
        else:
            self.q1.write(file)
            self.q2.write(file)
            self.q3.write(file)
            self.q4.write(file)


def encode(size, qt, path):
    # open file
    with open(path, "w") as f:
        f.write(str(size[0]) + " " + str(size[1]) + "\n")  # height width
        qt.write(f)


def main():
    img = cv2.imread(os.path.join(args["image"]))
    h, w, _ = img.shape

    max_depth = get_max_depth(img, int(args["depth"]))

    qt = ExportTree(img, (0, 0, w, h), 0, max_depth)

    encode((h, w), qt, args["encode"])


if __name__ == "__main__":
    main()
