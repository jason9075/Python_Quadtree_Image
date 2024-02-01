import argparse
import numpy as np
import cv2
import os

#  QuadTree Region
#
#  Quadrant 2 | Quadrant 1
#  -----------|-----------
#  Quadrant 3 | Quadrant 4
#

argparser = argparse.ArgumentParser()
argparser.add_argument("image", help="path to image")
argparser.add_argument(
    "-t", "--threshold", default=30, help="threshold for color difference"
)
argparser.add_argument("-d", "--depth", default=8, help="max depth of quadtree")
argparser.add_argument(
    "-l", "--line_thickness", default=1, help="line thickness of boundary"
)
argparser.add_argument("-o", "--output_name", default="output.jpg")

args = vars(argparser.parse_args())


class QuadTree:
    def __init__(self, image, boundary, depth, max_depth):
        self.boundary = boundary
        self.depth = depth
        self.color = None
        self.q1 = None
        self.q2 = None
        self.q3 = None
        self.q4 = None

        if (
            check_boundary(boundary)
            and check_color(image, boundary, int(args["threshold"]))
            and depth < max_depth
        ):
            self.subdivide(image, max_depth)
        else:
            self.color = average_color(image, boundary)

    def subdivide(self, image, max_depth):
        cx = int((self.boundary[0] + self.boundary[2]) / 2)
        cy = int((self.boundary[1] + self.boundary[3]) / 2)

        self.q2 = self.__class__(
            image,
            (self.boundary[0], self.boundary[1], cx - 1, cy - 1),
            self.depth + 1,
            max_depth,
        )
        self.q1 = self.__class__(
            image,
            (cx, self.boundary[1], self.boundary[2], cy - 1),
            self.depth + 1,
            max_depth,
        )
        self.q3 = self.__class__(
            image,
            (self.boundary[0], cy, cx - 1, self.boundary[3]),
            self.depth + 1,
            max_depth,
        )
        self.q4 = self.__class__(
            image,
            (cx, cy, self.boundary[2], self.boundary[3]),
            self.depth + 1,
            max_depth,
        )

    def draw(self, image, thickness):
        if self.color is not None:
            cv2.rectangle(
                image,
                (self.boundary[0], self.boundary[1]),
                (self.boundary[2], self.boundary[3]),
                self.color,
                cv2.FILLED,
            )
            # draw boundary
            if 0 < thickness:
                cv2.rectangle(
                    image,
                    (self.boundary[0], self.boundary[1]),
                    (self.boundary[2], self.boundary[3]),
                    (0, 0, 0),
                    thickness,
                )
        else:
            self.q1.draw(image, thickness)
            self.q2.draw(image, thickness)
            self.q3.draw(image, thickness)
            self.q4.draw(image, thickness)


def average_color(image, boundary):
    x1, y1, x2, y2 = boundary
    color = np.average(image[y1:y2, x1:x2], axis=(0, 1))
    return color.astype(np.uint8).tolist()


# return True if color diff greater than threshold
def check_color(image, boundary, thr):
    x1, y1, x2, y2 = boundary
    b, g, r = cv2.split(image[y1:y2, x1:x2])

    std_b = np.std(b)
    std_g = np.std(g)
    std_r = np.std(r)

    return std_b > thr or std_g > thr or std_r > thr


def check_boundary(boundary):
    x1, y1, x2, y2 = boundary
    return x2 - x1 > 2 and y2 - y1 > 2


def get_max_depth(image, user_assign):
    h, w, _ = image.shape

    # calc how many times v can be divided by 2
    min_size = min(h, w)
    max_depth = -1
    while min_size > 2:
        min_size /= 2
        max_depth += 1
    max_depth = min(max_depth, user_assign)
    return max_depth


def main():
    img = cv2.imread(os.path.join(args["image"]))
    h, w, _ = img.shape

    max_depth = get_max_depth(img, int(args["depth"]))
    qt = QuadTree(img, (0, 0, w, h), 0, max_depth)
    img_qt = np.zeros_like(img)
    qt.draw(img_qt, int(args["line_thickness"]))
    cv2.imwrite(os.path.join(args["output_name"]), img_qt)


if __name__ == "__main__":
    main()
