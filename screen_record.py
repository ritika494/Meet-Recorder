from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import cv2
import numpy as np


class Record():
    def __init__(self, object, file_name="video",size=None, flags=cv2.IMREAD_COLOR):
        self.object = object
        self.flags = flags
        self.size=size
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        if self.size is None:
            self.size = self.get_frame().shape[:2][::-1]
        self.out = cv2.VideoWriter(f"{file_name}.avi", fourcc, 2.0, self.size)

    def get_frame(self):
        try:
            if isinstance(self.object, WebDriver):
                im_arr = np.frombuffer(
                    self.object.get_screenshot_as_png(), dtype=np.uint8)
            elif isinstance(self.object, WebElement):
                im_arr = np.frombuffer(
                    self.object.screenshot_as_png, dtype=np.uint8)
        except:
            return False
        self.frame = cv2.imdecode(im_arr, flags=self.flags)
        return self.frame
    def capture(self):
        frame = cv2.resize(self.frame, self.size)
        self.out.write(frame)
        return frame

    def save(self):
        self.out.release()
 
       
