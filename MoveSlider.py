from selenium import webdriver
import time as t
import utility
import urllib

bg_img_dic = {}
slider_img_dic = {}
m = 0

def move_slider(distance):

    # launch firefox
    dr = webdriver.Firefox(executable_path=utility.firefox_driver_path)

    # start firefox
    dr.get(utility.url)

    # find two elements
    bg_img_element = dr.find_element_by_xpath(utility.bg_xpath)
    slider_img_element = dr.find_element_by_xpath(utility.slider_xpath)

    # get url of two elements
    bg_img_url = bg_img_element.get_attribute('src')
    slider_img_url = slider_img_element.get_attribute('src')

    global bg_img_dic, slider_img_dic, m

    if bg_img_url != None and not bg_img_url in bg_img_dic:

        bg_img_ext = bg_img_url.split('.')[-1]                      # .jpg
        slider_img_ext = slider_img_url.split('.')[-1]              # .png

        bg_file_name = str(m) + '.' + bg_img_ext
        slider_file_name = str(m) + '.' + slider_img_ext

        # save image file
        bg_file_data = urllib.request.urlopen(bg_img_url).read()
        slider_file_data = urllib.request.urlopen(slider_img_url).read()

        f_bg = open(utility.bg_img_file + bg_file_name, 'wb')
        f_slider = open(utility.slider_img_file + slider_file_name, 'wb')

        f_bg.write(bg_file_data)
        f_slider.write(slider_file_data)

        f_bg.close()
        f_slider.close()

        m += 1

