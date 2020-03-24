import winreg
import admin
import os

#print(0)
if not admin.isUserAdmin():
    admin.runAsAdmin(wait=False)
    exit()
#print(0.5)


REG_PATH = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\0001"

def set_reg(name, value):
    #try:
    winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
    registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0, 
                                   winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
    winreg.CloseKey(registry_key)
    return True
    #except WindowsError:
    #    return False

def get_reg(name):
    try:
        
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0,
                                       winreg.KEY_READ)
        
        value, regtype = winreg.QueryValueEx(registry_key, name)
        
        winreg.CloseKey(registry_key)
        
        return value
    except WindowsError:
        return None


#print (get_reg('MouseSensitivity'))

mac = input("Mac Address: R for random, D for default or type one in:\n")
if mac.lower() == "r":
    b = list("ABCDEF1234567890")
    c = list("26AE")
    import random
    mac = ""
    for i in range(0,12):
        if i == 1:
            mac += random.choice(c)
            continue
        mac += random.choice(b)

if mac.lower() == "d":
    mac = ""
d = ""
for i in mac:
    if not (i == ":" or i == "."):
        d += i
mac = d
set_reg('NetworkAddress',mac)
os.system("netsh interface set interface \"Wi-Fi\" disable")
os.system("netsh interface set interface \"Wi-Fi\" enable")
input("Done")


