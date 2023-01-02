#==============================================================================
# Drakar och Demoner Assistent (DoDA)
# Copyright (C) 2022  Henric Zazzi <hzazzi@kth.se>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#==============================================================================
import wx
import datetime
import Config
#------------------------------------------------------------------------------
class charFrame(wx.Frame):
  panel = None
  nametext = None
  actext = None
  wptext = None
  chartext = None
  onOk = False
#------------------------------------------------------------------------------
  def __init__(self):
    super().__init__(None, title=Config.LANG.EVENT, size=(450, 470))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    self.panel.SetBackgroundColour(wx.Colour(230, 230, 255))
    lbl1 = wx.StaticText(self.panel, pos = (50, 30), size = (150,20), label = Config.LANG.CHARNAME)
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    lbl2 = wx.StaticText(self.panel, pos = (50, 65), size = (150,20), label = Config.LANG.CHARAC)
    lbl2font = self.GetFont() 
    lbl2font.SetWeight(wx.BOLD)
    lbl2.SetFont(lbl2font)
    lbl3 = wx.StaticText(self.panel, pos = (50, 100), size = (150,20), label = Config.LANG.CHARWP)
    lbl3font = self.GetFont() 
    lbl3font.SetWeight(wx.BOLD)
    lbl3.SetFont(lbl3font)
    lbl4 = wx.StaticText(self.panel, pos = (50, 135), size = (150,20), label = Config.LANG.CHARTEXT)
    lbl4font = self.GetFont() 
    lbl4font.SetWeight(wx.BOLD)
    lbl4.SetFont(lbl4font)
    button1 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.OK, (130, 390))
    button2 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.CANCEL, (230, 390))
    button1.Bind(wx.EVT_BUTTON, self.onButton1) 
    button2.Bind(wx.EVT_BUTTON, self.onButton2)     
#------------------------------------------------------------------------------
  def setValues(self, name, ac, wp, text):
    self.nametext = wx.TextCtrl(self.panel, wx.ID_ANY, name, pos = (150, 25), size=(250, -1))
    self.actext = wx.TextCtrl(self.panel, wx.ID_ANY, str(ac), pos = (150, 60), size=(250, -1))
    self.wptext = wx.TextCtrl(self.panel, wx.ID_ANY, str(wp), pos = (150, 95), size=(250, -1))
    self.chartext = wx.TextCtrl(self.panel, wx.ID_ANY, text, pos = (50, 160), size=(350, 200), style= wx.TE_MULTILINE)
#------------------------------------------------------------------------------
  def onButton1(self, event):
    self.onOk = True
    self.Hide()
#------------------------------------------------------------------------------
  def onButton2(self, event):
    self.Hide()
#------------------------------------------------------------------------------

