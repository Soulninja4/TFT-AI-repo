import mouse_events
from win32gui import FindWindow, GetWindowRect

def getWindowDimensions():
    window_handle = FindWindow(None, "League of Legends (TM) Client")
    rect = GetWindowRect(window_handle)

    x1 = rect[0]
    y1 = rect[1] 
    x2 = rect[2] 
    y2 = rect[3] 

    return x1, y1, x2, y2


def main():
    x1, y1, x2, y2 = getWindowDimensions()

    