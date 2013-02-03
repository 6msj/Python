# frame options, first three required
wx.Frame(wx.Window parent, int id=-1, string title='', wx.Point pos = wx.DefaultPosition, 
  wx.Size size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE, string name = "frame")

# methods
Move(wx.Point point) #move a window to the given position
MoveXY(int x, int y) #move a window to the given position
SetPosition(wx.Point point) #set the position of a window
SetDimensions(wx.Point point, wx.Size size) #set the position and the size of a window
Maximize() #maximizes
Centre() #centers
