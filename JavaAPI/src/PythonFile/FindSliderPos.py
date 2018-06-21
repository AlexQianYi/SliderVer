import CalSliderSize
import cv2
import HashCompareImg


def find_slider_position(slider_img, bg_img):

    slider_x, slider_y, slider_height,slider_width = 0,0,0,0
    slider_x, slider_y, slider_height, slider_width = CalSliderSize.calculate_slider_size(slider_img)

    # cut slider image
    slider_cut_img = slider_img[slider_y+20:slider_y+40, slider_x+20:slider_x+40]

    bg_y, bg_x, bg_channel = bg_img.shape

    minHash = 20*20
    minIndex = 20

    hash1 = HashCompareImg.aHash(slider_cut_img)

    for i in range(20, bg_x-20):

        info = "Find position: " + str(i) + '*' + str(slider_y)
        print(info)
        bg_cut_img = bg_img[slider_y+20:slider_y+40, i:i+20]
        hash2 = HashCompareImg.aHash(bg_cut_img)
        n = HashCompareImg.cmpHash(hash1, hash2)
        if n<minHash:
            minHash = n
            minIndex = i-20

    return minIndex

"""
if __name__ == '__main__':

    # single image file
    slider_img = cv2.imread('./SliderImg/2.png')

    # bg image
    bg_image = cv2.imread('./BgImg/2.jpg')

    find_slider_position(slider_img, bg_image)
"""


