from PIL import ImageGrab
import os
import time
from win32gui import FindWindow, GetWindowRect
import ctypes
import mouse_events
 
def screenGrab():
    window_handle = FindWindow(None, "League of Legends (TM) Client")
    rect = GetWindowRect(window_handle)

    x1 = rect[0]
    y1 = rect[1] 
    x2 = rect[2] 
    y2 = rect[3] 

    box = (x1, y1, x2, y2)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
    '.png', 'PNG')
 
def getWindowDimensions():
    window_handle = FindWindow(None, "League of Legends (TM) Client")
    rect = GetWindowRect(window_handle)

    x1 = rect[0]
    y1 = rect[1] 
    x2 = rect[2] 
    y2 = rect[3] 

    return x1, y1, x2, y2


def main():
    pass
 
if __name__ == '__main__':
    main()