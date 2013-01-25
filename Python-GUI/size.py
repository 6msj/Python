# size.py

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                size=(600, 200)) #width x height
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
