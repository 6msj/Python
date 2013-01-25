# simple.py

import wx # import wx

app = wx.App() # set the app to be the wx.App

frame = wx.Frame(None, -1, 'simple.py') # creates a frame, parent widget 
frame.Show() # Show() method displays the frame

app.MainLoop() # MainLoop() is an endless cycle
