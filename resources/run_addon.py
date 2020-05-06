import sys
import xbmcaddon
import xbmcplugin
import xbmcgui

import directoryUtils

from globals import g

def run(argv):
    addon       = xbmcaddon.Addon()
    addonId     = int(sys.argv[1])
    g.initGlobals(argv)
    # Launch a dialog box in kodi showing the string variable 'line1' as the contents
    # url = 'https://www.quebec511.info/camera.ashx?id=3604&format=mp4'
    # li = xbmcgui.ListItem('My First Video!', iconImage='DefaultVideo.png')
    # video_info = {
    #     'codec': 'h264',
    #     'aspect': 1.78,
    #     'width': 1280,
    #     'height': 720,
    # }
    # li.addStreamInfo('video', video_info)
 
    if argv[2] != '':
        print("#########################################################################################")
        camList = directoryUtils.createCameraList()
        xbmcplugin.addDirectoryItems(addonId, camList)
    else:
        regionList = directoryUtils.createRegionList()
        xbmcplugin.addDirectoryItems(addonId, regionList)


    xbmcplugin.endOfDirectory(addonId)