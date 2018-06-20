from selenium import webdriver
import utility
import urllib
import cv2
import FindSliderPos
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

bg_img_dic = {}
slider_img_dic = {}
m = 0

def calculate_distance():

    
    try:
        # launch firefox
        dr = webdriver.Firefox(executable_path=utility.firefox_driver_path)

        # start firefox
        dr.get(utility.url)
    
    except:
        print('browser open fail')
    else:
        print('browser open succeed')


    try:
        # find two elements
        bg_img_element = dr.find_element_by_xpath(utility.bg_xpath)
        slider_img_element = dr.find_element_by_xpath(utility.slider_xpath)
    
        # get url of two elements
        bg_img_url = bg_img_element.get_attribute('src')
        slider_img_url = slider_img_element.get_attribute('src')
        
    except:
        print('find two eles fail')
    else:
        print('find two eles succeed')

    global bg_img_dic, slider_img_dic, m

    if bg_img_url != None and not bg_img_url in bg_img_dic:

        bg_img_ext = bg_img_url.split('.')[-1]                      # .jpg
        slider_img_ext = slider_img_url.split('.')[-1]              # .png

        bg_file_name = str(m) + '.' + bg_img_ext
        slider_file_name = str(m) + '.' + slider_img_ext

        # save image file
        bg_file_data = urllib.request.urlopen(bg_img_url).read()
        slider_file_data = urllib.request.urlopen(slider_img_url).read()

        bg_path = utility.bg_img_file + bg_file_name
        slider_path = utility.slider_img_file + slider_file_name

        f_bg = open(bg_path, 'wb')
        f_slider = open(slider_path, 'wb')

        f_bg.write(bg_file_data)
        f_slider.write(slider_file_data)

        m += 1

        f_bg.close()
        f_slider.close()

        print(bg_path, slider_path)
        # single image file
        slider_img = cv2.imread(slider_path)

        # bg image
        bg_image = cv2.imread(bg_path)

        #cv2.imshow("bg", bg_image)
        #cv2.imshow("slider", slider_img)
        #cv2.waitKey(0)

        distance = FindSliderPos.find_slider_position(slider_img, bg_image)
        print(distance)

        bg_img_dic[bg_img_url] = distance

    else:
        distance = bg_img_dic[bg_img_url]


    #move_slider(dr, distance/2)


def move_slider(dr, distance):

    slider_bottom = dr.find_element_by_xpath(utility.slider_button_xpath)
    action = ActionChains(dr)
    action.click_and_hold(slider_bottom).perform()


    """
    try:
        action.move_by_offset(distance+20, 0).perform()
    except UnexpectedAlertPresentException:
        pass
    """


    while distance>20:
        try:
            action.move_by_offset(20, 0).perform()
            distance -= 20
        except UnexpectedAlertPresentException:
            break

    while distance>10:
        try:
            action.move_by_offset(10, 0).perform()
            distance -= 10
        except UnexpectedAlertPresentException:
            break

    while distance>3:
        try:
            action.move_by_offset(3, 0).perform()
            distance -= 3
        except UnexpectedAlertPresentException:
            break

    slider_bottom.click()


    print('click finish')







if __name__ == '__main__':

    print('b')

    #calculate_distance()