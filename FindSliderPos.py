import CalSliderSize
import cv2

if __name__ == '__main__':

    # single image file
    slider_img = cv2.imread('./Slider/1.png')

    slider_x, slider_y, slider_height,slider_width = 0,0,0,0

    slider_x, slider_y, slider_height, slider_width = CalSliderSize.calculate_slider_size(slider_img)