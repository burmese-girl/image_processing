import cv2
import numpy as np
import os

mypath = os.path.dirname(os.path.abspath(__file__))


def count_pixels():
    img = cv2.imread(mypath + '/Question2/sample.png')
    # boundaries for the color red
    boundaries = [([0, 0, 130], [80, 80, 255]), ]
    # boundaries for the color green
    green_boundaries = [([0, 120, 0], [60, 255, 60])]
    # boundaries for the color blue
    blue_boundaries = [([100, 0, 0], [255, 90, 90])]

    for (lower, upper) in boundaries:
        # creates numpy array from boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(img, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)

        # background white for red_mask
        bk = np.full(img.shape, 255, dtype=np.uint8)  # white background
        bk_red_mask = cv2.bitwise_not(mask)
        bk_masked_red = cv2.bitwise_and(bk, bk, mask=bk_red_mask)
        red_final = cv2.bitwise_or(output, bk_masked_red)

    for (lower, upper) in green_boundaries:
        # creates numpy array from boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(img, lower, upper)
        output_green = cv2.bitwise_and(img, img, mask=mask)

    for (lower, upper) in blue_boundaries:
        # creates numpy array from boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # finds colors in boundaries a applies a mask
        mask = cv2.inRange(img, lower, upper)
        output_blue = cv2.bitwise_and(img, img, mask=mask)

    # summed = np.sum(output, axis=2)
    tot_pixel = output.size
    red_pixel = np.count_nonzero(output)
    green_pixel = np.count_nonzero(output_green)
    blue_pixel = np.count_nonzero(output_blue)

    print("red :  " + str(red_pixel) + " pixels")
    print("green :  " + str(green_pixel) + " pixels")
    print("blue :  " + str(blue_pixel) + " pixels")


count_pixels()
