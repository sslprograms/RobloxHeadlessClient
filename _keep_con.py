import subprocess, sys, pygetwindow, time, threading, psutil 

# This lowers the Graphics and CPU/RAM usage 

# def options(window):
#     # window.toSize(0,0)
#     window.hide()
#     window.minimize()
#     subprocess.getoutput('taskkill /f /im RobloxPlayerLauncher.exe')

# def keep_invisible():

#     while True:
#         subprocess.getoutput('taskkill /f /im RobloxPlayerLauncher.exe')
#         try:
#             windows = pygetwindow.getAllWindows()

#             for window in windows:
#                 if window.title == 'Roblox':
#                     threading.Thread(target=options,args=(window,)).start()

#                 if window.title == 'Roblox Game Client':
#                     threading.Thread(target=options,args=(window,)).start()
                
#                 time.sleep(0.05)
#         except:
#             pass


# if __name__ == '__main__':

#     arguments = sys.argv[1:]

#     for arg in arguments:
#         if arg == '.loop':
#             keep_invisible()