import cv2
from PIL import Image
import CompareImg


def calculate_slider_size(img):

    """
    calculate the parameters of slider image
    :param img: slider image file
    :return:  the x,y,height,width of slider image
    """

    rows, cols, channels = img.shape
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


def temp():

    slider_img = cv2.imread('./SliderImg/1.png')
    bg_img = cv2.imread('./BgImg/1.jpg')






    # find top of ear
    for i in range(rows):
        find = False
        for j in range(cols):
            if slider_img[i, j][0] !=0 or slider_img[i, j][1] !=0 or slider_img[i,j][2] != 0:
                find = True
        if find:
            ear_top = i
            break

    # find left of ear
    for j in range(cols-1, square_right, -1):
        find = False
        for i in range(rows):
            if slider_img[i, j][0] !=0 or slider_img[i, j][1] !=0 or slider_img[i,j][2] != 0:
                find = True
        if find:
            ear_right = j
            break

    #print(square_top, square_bottom, square_left, square_right)
    #print(ear_top, ear_right)


    square_start_top = square_top
    square_start_left = square_left
    bg_start_top = 162+20
    bg_start_left = 164+20

    slider_R_point = []
    bg_R_point = []

    """
    for i in range(20):
        for j in range(20):

            print(slider_img[square_start_top + i, square_start_left + j], bg_img[bg_start_top + i, bg_start_left + j])

    """
    slider_x = square_start_left
    slider_y = square_start_top
    w = 60
    h = 60
    bg_x = bg_start_left
    bg_y = bg_start_top

    slider_img = Image.open('./SliderImg/1.png')
    #bg_img = Image.open('./BgImg/1.jpg')

    cut_slider = slider_img.crop((slider_x, slider_y, slider_x+w, slider_y+h))
    #cut_bg = bg_img.crop((bg_x, bg_y, bg_x+w, bg_y+h))

    cut_slider.show()
    #cut_bg.show()

    cut_slider.save('./3.png',)
    #cut_bg.save('./2.jpg',)

def visit_bg_image():

    start_x = 20
    start_y = 162+20

    end_left = 480-60

    slider_x = square_start_left
    slider_y = square_start_top
    w = 20
    h = 20

    slider_img = Image.open('./SliderImg/1.png')

    cut_slider = slider_img.crop((slider_x, slider_y, slider_x+w, slider_y+h))
    cut_slider.save('./3.png', )

    minIndex = 20
    minHash = 400

    img1 = cv2.imread('./1.png')

    hash1 = CompareImg.aHash(img1)

    for i in range(end_left):
        print('compare: '+str(i))
        bg_img = Image.open('./BgImg/1.jpg')
        cut_bg = bg_img.crop((start_x+i, start_y, start_x+i+20, start_y+20))
        cut_bg.save('./CutBg/'+str(i)+'.png')
        img2 = cv2.imread('./CutBg/'+str(i)+'.png')
        hash2 = CompareImg.aHash(img2)
        n = CompareImg.cmpHash(hash1, hash2)
        print(n)
        if n<minHash:
            minHash = n
            minIndex = 20+i

    print(minHash, minIndex)



if __name__ == "__main__":

    visit_bg_image()
    #calculate_slider_size()