import cv2
from PIL import Image
import HashCompareImg


def calculate_slider_size(slider_img):

    """
    calculate the parameters of slider image
    :param img: slider image file
    :return:  the x,y,height,width of slider image
    """

    rows, cols, channels = slider_img.shape
    square_top, square_bottom, square_left, square_right = 0, 0, 0, 0

    # find top of square
    for i in range(1, rows):
        count = 0
        for j in range(cols):

            if (slider_img[i, j][0] !=0 or slider_img[i, j][1] !=0 or slider_img[i,j][2] != 0 ) and \
                    (slider_img[i-1, j][0] == 0 and slider_img[i-1, j][1] == 0 and slider_img[i-1, j][2] == 0):
                count += 1

        if count >20:
            square_top = i
            break

    # find bottom of square
    for i in range(square_top, rows):
        count = 0
        for j in range(cols):

            if (slider_img[i, j][0] !=0 or slider_img[i, j][1] !=0 or slider_img[i,j][2] != 0 ) and \
                    (slider_img[i+1, j][0] == 0 and slider_img[i+1, j][1] == 0 and slider_img[i+1, j][2] == 0):
                count += 1

        if count >20:
            square_bottom = i
            break

    # find left of square
    for j in range(1, cols):
        count = 0
        for i in range(rows):

            if (slider_img[i, j][0] !=0 or slider_img[i, j][1] !=0 or slider_img[i,j][2] != 0 ) and \
                    (slider_img[i, j-1][0] == 0 and slider_img[i, j-1][1] == 0 and slider_img[i, j-1][2] == 0):
                count += 1

        if count >20:
            square_left = j
            break

    # find right of square
    for j in range(square_left, cols):
        count = 0
        for i in range(rows):

            if (slider_img[i, j][0] != 0 or slider_img[i, j][1] != 0 or slider_img[i, j][2] != 0) and \
                    (slider_img[i, j +1][0] == 0 and slider_img[i, j + 1][1] == 0 and slider_img[i, j + 1][2] == 0):
                count += 1

        if count > 20:
            square_right = j
            break


    return square_left, square_top, square_bottom-square_top, square_right-square_left
