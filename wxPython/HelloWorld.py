<<<<<<< HEAD
import wx
class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello World')
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
=======
import wx
class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello World')
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
>>>>>>> f4cdb409395ff24a97c09e23a589aab0beb3dd72
    app.MainLoop()