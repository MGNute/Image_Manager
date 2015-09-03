__author__ = 'Michael'

import wx
import main.gui_manager

if __name__ == '__main__':
    app = main.gui_manager.MyApp()
    # top = main.gui_manager.gui_manager(None)
    # top.Show(True)
    # print wx.GetTopLevelWindows()
    app.MainLoop()
    # print wx.GetTopLevelWindows()
