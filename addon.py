import sys
import xbmcaddon
import xbmcplugin
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonId     = int(sys.argv[1])

# Launch a dialog box in kodi showing the string variable 'line1' as the contents
url = 'https://www.quebec511.info/camera.ashx?id=3604&format=mp4'
li = xbmcgui.ListItem('My First Video!', iconImage='DefaultVideo.png')
video_info = {
    'codec': 'h264',
    'aspect': 1.78,
    'width': 1280,
    'height': 720,
}
li.addStreamInfo('video', video_info)
xbmcplugin.addDirectoryItem(handle=addonId, url=url, listitem=li)


xbmcplugin.endOfDirectory(addonId)