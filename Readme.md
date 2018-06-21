# Demo of Recognition Slide Verification Code API

## 1. Environment


Java. Python.

### Test Python Version

Python 3.6

### Required Python Modules (Need installed)

OpenCV / cv2 

	Computer Vision library, which include lots of general computer vision algorithms, can be applied by Python, Ruby, MATLAB etc.
	
	
selenium

	Selenium is a web application test system, which include tset record (selenium IDE), complie and run (Selenium Remote Control) and parallel test (Selenium Grid).
	
	We primary use Webdriver in selenium to write Python spider.
	
	Selenium.Webdriver can be used in these browsers:
	android; blackberry; chrome; common; edge; firefox; ie; opera; phantomjs; remote; safari; support.
	

## 2. Encapsulate Python Script

###Runtime
	
Use Runtime to simulate execute terminal command. Two parameters are neccessary (Need to change):

	(1) Python path (the Python which already installed required modules). e.g.:
	"/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/bin/python3.6"
	
	(2) Python file path. e.g.:
	"/Users/yiqian/Documents/GitHub/SliderVer/JavaAPI/src/PythonFile/MoveSlider.py"

Python Main file:	

	MoveSlider.py

## 3. Java API Parameters

###Input

String url

	The URL of website which has slide verification code need to be recognized.
	
	default: "https://id.163yun.com/login?referrer=https://dun.163.com/dashboard&h=yd&fromyd=baiduP2_YZM_CP1934"
	
String xpathBG
	
	The xpath expression of background image. (Can find by Chrome developer mode)
	
	default: "//*[@id=\"bg\"]/div[2]/div/div/div/div/div[1]/form/div[3]/div/div/div[1]/div/div[1]/img[1]"
	
String xpathSlider

	The xpath expression of slider image. (Can find by Chrome developer mode)
	
	default: "//*[@id=\"bg\"]/div[2]/div/div/div/div/div[1]/form/div[3]/div/div/div[1]/div/div[1]/img[2]"
	
###Output
int getMove_distance

	return the number of pixel slide need to move to finish recognition.
	
## 4. Others (Need to change)
###FireFox Driver Path
	
To launch different browsers by selenium, we need point out browser's driver path. 

	src -> PythonFile -> utility.py 
	change (firefox_driver_path) 

### Background Image File Path

To analyze images we need download images to local first. 

	src -> PythonFile -> utility.py
	change (bg_img_file)
	
### Slider Image File Path
	
	src -> PythonFile -> utility.py
	change (slider_img_file)
	
## 5. Tips
### Python Install
Easy Install Python by **Anaconda**, then install required modules:
	
	conda install 
	

