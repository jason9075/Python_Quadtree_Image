# Python QuadTree Image Segmentation

## Overview

This Python script implements a quadtree-based image segmentation algorithm. It subdivides an image into smaller regions based on color variation and represents these regions using a quadtree data structure. The script allows customization of various parameters such as color difference threshold, maximum depth of the quadtree, and boundary line thickness.

## Requirements

- Python 3.x
- OpenCV library
- NumPy library

## Usage

Run the script from the command line by providing the path to the image and optional arguments for threshold, depth, line thickness, and output file name.

```
python main.py [path_to_image] [optional_arguments]
```

### Optional Arguments

- `-t` or `--threshold`: Sets the threshold for color difference (default: 30)
- `-d` or `--depth`: Sets the maximum depth of the quadtree (default: 8)
- `-l` or `--line_thickness`: Sets the line thickness for drawing boundaries (default: 1)
- `-o` or `--output_name`: Sets the name of the output image file (default: "output.jpg")

## Example

```
python main.py images/DALLE_AI_IMAGE_1.jpg -o images/QUAD_1.jpg
```

<!-- readme image-->

![](/images/QUAD_1.jpg)

```
python main.py images/DALLE_AI_IMAGE_2.jpg -o images/QUAD_2.jpg
```

<!-- readme image-->

![](/images/QUAD_2.jpg)

## Article

[ Medium 使用Quadtree對圖片進行壓縮的一些實驗 ](https://medium.com/@capillaryj/python-%E4%BD%BF%E7%94%A8quadtree%E5%B0%8D%E5%9C%96%E7%89%87%E9%80%B2%E8%A1%8C%E5%A3%93%E7%B8%AE%E7%9A%84%E4%B8%80%E4%BA%9B%E5%AF%A6%E9%A9%97-68b1fc132ab0)

## Ref

1. [ Insane Huge Terrain 10,000 square km - Godot engine ](https://www.youtube.com/watch?v=nFzaRfreD_o)

2. [ Coding Challenge #98.1: Quadtree - Part 1 ](https://www.youtube.com/watch?v=OJxEcs0w_kE)

3. [ Quadtrees in Unity are AMAZING ](https://www.youtube.com/watch?v=OquPzambxFA)

## License

[MIT License](LICENSE)
