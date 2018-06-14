import cv2
import aircv as ac
from PIL import Image
from PIL import ImageChops

def draw_circle(img, pos, circle_radius, color, line_width):

    cv2.circle(img, pos, circle_radius, color, line_width)
    cv2.imshow('objDetect', imsrc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':


    img = cv2.imread('./BgImg/1.jpg')
    slider = cv2.imread('./SliderImg/1.png')

    cv2.imshow('slider', slider)
    cv2.imshow('img', img)

    rows, cols, channels = img.shape
    dst = img.copy()

    a = 1.2
    b = 100

    print(img[0,0])
    print(img[0,1])

    for i in range(rows):
        for j in range(cols):
            for c in range(3):
                color = img[i, j][c] *a + b
                if color>255:
                    dst[i,j][c] = 255
                elif color<0:
                    dst[i,j][c]=0

    cv2.imshow('dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""
    imsrc = Image.open('./BgImg/1.jpg')
    imobj = Image.open('./SliderImg/1.png')

    

    height, width = imobj.height, imobj.width

    print(imobj.getpixel((12, 160)), imobj.getpixel((60, 160)), imobj.getpixel((12, 216)), imobj.getpixel((60, 216)))
    print(imsrc.getpixel((171, 169)), imsrc.getpixel((219, 169)), imsrc.getpixel((171, 218)), imsrc.getpixel((219, 218)))

    imsrc = ac.imread('./BgGreyImg/1.jpg')
    imobj = ac.imread('./SliderGreyImg/1.jpg')




    # find position
    pos = ac.find_template(imsrc, imobj)

    circle_center_pos = pos['result']
    circle_radius = 50
    color = (0, 255, 0)
    line_width = 5

    draw_circle(imsrc, circle_center_pos, circle_radius, color, line_width)
"""


