from winreg import *
import os
#system id to user
def sid_to_user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows_NT\CurrentVersion\ProfileList" + '\\' + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid
    
#get directory
def return_dir():
    dirs = ['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

#find files
def find_recycled(recycleDir):
    dir_list = os.listdir(recycleDir)
    for sid in dir_list:
        files = os.listdir(recycleDir + sid)
        user = sid_to_user(sid)
        print('\n[*] Listing Files For User: ' + str(user))
        for file in files:
            print('[+] Found File: ' + str(file))


if __name__ == '__main__':
    recycle_dir = return_dir()
    find_recycled(recycle_dir)