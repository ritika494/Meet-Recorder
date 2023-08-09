# import required modules
# from pyvda import AppView, get_apps_by_z_order, VirtualDesktop, get_virtual_desktops
from selenium import webdriver
# from screen_record import Record # Import Record class from selenium_addons.py file which contain above code
# from audio_record import audioRecord
# import asyncio
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# import multiprocessing
import threading
# from queue import Queue
# from subprocess import Popen
# from subprocess import call

import time

# import pyautogui
# import cv2
# import numpy as np

service = Service(
    "C:/Users/Roshan Yadav/Documents/chromedriver_win32/chromedriver.exe")


def Glogin(mail_address, password):
	# Login Page
	driver.get(
		'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

	# input Gmail
	driver.find_element(By.ID, "identifierId").send_keys(mail_address)
	driver.find_element(By.ID, "identifierNext").click()
	driver.implicitly_wait(10)

	# input Password
	driver.find_element(By.ID,
		'password').send_keys(password)
	driver.implicitly_wait(10)
	driver.find_element(By.ID, "passwordNext").click()
	driver.implicitly_wait(10)
 	
	print("successfully logged into google account")

	# go to google home page
	driver.get('https://google.com/')
	driver.implicitly_wait(100)
	print("opening google-meet")
	


def turnOffMicCam():
	# turn off Microphone
    # print("turning off mic")
    # time.sleep(5)
    # driver.find_element(By.XPATH,
	#     '/html/body/div[1]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[5]/div[1]/div/div[1]/div[1]').click()
    # driver.implicitly_wait(3000)
    # print(105)
	# # turn off camera
    # time.sleep(3)
    # print("turning off cam")
    # driver.find_element(By.CSS_SELECTOR,
	# 	'div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.M9Bg4d.HNeRed').click()
    # driver.implicitly_wait(3000)
    print("joining meet")
    


def joinNow():
	# Join meet
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,
		'button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.jEvJdc.QJgqC').click()
    driver.implicitly_wait(12600)
    print("joined meeting")


def AskToJoin():
	# Ask to Join meet
	time.sleep(5)
	driver.implicitly_wait(2000)
	driver.find_element(By.CSS_SELECTOR,
		'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt')
    
	# Ask to join and join now buttons have same xpaths
def terminate(process):
    if process.poll() is None:
        call('taskkill /F /T /PID ' + str(process.pid))
# assign email id and password
mail_address = 'ritik0050.cse19@chitkara.edu.in'
password = 'Ritik@12345432'



# create chrome instance

driver_exe = 'chromedriver'
options = Options()
options.add_argument("--headless")


# opt = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--start-maximized')

options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_argument('--window-size=1920,1080')
options.add_experimental_option("prefs", {
	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(driver_exe, options=options,service=service)

window = Record(driver, file_name="screenRecording")
Glogin(mail_address, password)


driver.get('https://meet.google.com/dam-gffj-phr')
turnOffMicCam()

# Join()
joinNow()
time.sleep(7)

# audioRecord()

# def screenRecord():
# 	print("screen recording starts")   
# 	i=0
# 	while True:
# 		i=i+1
# 		print(i)
# 		frame = window.get_frame()
# 		if i==25:
# 			window.save()
# 			break
# 		window.capture()
# 	print("screen recording stops")
# screenRecord()
 
# if name== 'main' :
# p1=threading.Thread(target=audioRecord)
# p1.start()
# p2=threading.Thread(target=screenRecord)
# p2.start()
# p1.join()
# p2.join()	

# if _name_ == "_main_":
# 	loop = asyncio.new_event_loop()
# 	asyncio.set_event_loop(loop)
# 	loop.run_until_complete(asyncio.gather(audioRecord(), screenRecord()))

print("succesfully left the meeting")