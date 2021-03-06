import win32api, win32con
import time

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")         #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')

def rightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    print("Click.")         #completely optional. But nice for debugging purposes.

def rightDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    print('left Down')
         
def rightUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    time.sleep(.1)
    print('left release')

def mousePos(x1, y1, cord): #relative to top left of game window where x1, y1 = top left; cord = coordinates we want to move the mouse to
    pos = (x1 + cord[0], y1 + cord[1])
    win32api.SetCursorPos(pos)
     
def get_cords(x1,y1):
    x,y = win32api.GetCursorPos()
    x = x - x1
    y = y - y1
    print(x,y)