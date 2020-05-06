import win32gui
import win32con
import win32api
def setPos(x,y):
    win32api.SetCursorPos((int(x),int(y)))

def changePos(x,y):
    a = getPos()
    win32api.SetCursorPos((int(a[0]+x),int(a[1]+y)))
    
def getPos():
    return win32gui.GetCursorPos()

def click(x=None,y=None,button="left"):
    if x == None:
        a = getPos()
        x = a[0]
        y = a[1]
    if button == "left":
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    if button == "right":
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

    if button == "middle":
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,x,y,0,0)
