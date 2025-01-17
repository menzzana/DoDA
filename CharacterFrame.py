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
import Config
#------------------------------------------------------------------------------
class CharacterFrame(wx.Frame):
  panel = None
  nametext = None
  hptext = None
  actext = None
  chartext = None
  onOk = False
#------------------------------------------------------------------------------
  def __init__(self):
    super().__init__(None, title=Config.LANG.CHARS, size=(400, 450))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    self.panel.SetBackgroundColour(wx.Colour(230, 230, 255))
    lbl1 = wx.StaticText(self.panel, pos = (10, 30), size = (150,20), label = Config.LANG.NAME)
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    lbl5 = wx.StaticText(self.panel, pos = (10, 65), size = (150,20), label = Config.LANG.CHARLIFE)
    lbl5.SetFont(lbl1font)
    lbl2 = wx.StaticText(self.panel, pos = (10, 100), size = (150,20), label = Config.LANG.CHARAC)
    lbl2.SetFont(lbl1font)
    lbl4 = wx.StaticText(self.panel, pos = (10, 135), size = (150,20), label = Config.LANG.CHARTEXT)
    lbl4.SetFont(lbl1font)
    button1 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.OK,  pos = (40, 380))
    button2 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.CANCEL, pos = (230, 380))
    button1.Bind(wx.EVT_BUTTON, self.onButton1) 
    button2.Bind(wx.EVT_BUTTON, self.onButton2)     
#------------------------------------------------------------------------------
  def setClearValues(self):
    self.setValues('', 0, 0, '')
#------------------------------------------------------------------------------
  def setValues(self, name, hp, ac, text):
    self.nametext = wx.TextCtrl(self.panel, wx.ID_ANY, name, pos = (150, 25), size=(240, -1))
    self.hptext = wx.TextCtrl(self.panel, wx.ID_ANY, str(hp), pos = (150, 60), size=(240, -1))
    self.actext = wx.TextCtrl(self.panel, wx.ID_ANY, str(ac), pos = (150, 95), size=(240, -1))
    self.chartext = wx.TextCtrl(self.panel, wx.ID_ANY, text, pos = (10, 165), size=(380, 200), style= wx.TE_MULTILINE)
#------------------------------------------------------------------------------
  def onButton1(self, event):
    self.onOk = True
    self.Hide()
#------------------------------------------------------------------------------
  def onButton2(self, event):
    self.Hide()
#------------------------------------------------------------------------------
