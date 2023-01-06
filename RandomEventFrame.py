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
class RandomEventFrame(wx.Frame):
  panel = None
  titletext = None
  distmintext = None
  distmaxtext = None
  hptext = None
  attitudeidx = None
  text = None
  onOk = False
#------------------------------------------------------------------------------
  def __init__(self):
    super().__init__(None, title=Config.LANG.RANDOMEVENTTEXT, size=(400, 470))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    self.panel.SetBackgroundColour(wx.Colour(230, 230, 255))
    lbl1 = wx.StaticText(self.panel, pos = (10, 30), size = (150,20), label = Config.LANG.TITLE)
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    lbl5 = wx.StaticText(self.panel, pos = (10, 65), size = (150,20), label = Config.LANG.DISTANCE)
    lbl5.SetFont(lbl1font)
    lbl6 = wx.StaticText(self.panel, pos = (270, 65), size = (20,20), label = Config.MINUS)
    lbl6.SetFont(lbl1font)
    lbl2 = wx.StaticText(self.panel, pos = (10, 95), size = (150,20), label = Config.LANG.CHARHP)
    lbl2.SetFont(lbl1font)
    lbl3 = wx.StaticText(self.panel, pos = (10, 130), size = (150,20), label = Config.LANG.ATTITUDE)
    lbl3.SetFont(lbl1font)
    lbl4 = wx.StaticText(self.panel, pos = (10, 165), size = (150,20), label = Config.LANG.CHARTEXT)
    lbl4.SetFont(lbl1font)
    button1 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.OK,  pos = (40, 400))
    button2 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.CANCEL, pos = (230, 400))
    button1.Bind(wx.EVT_BUTTON, self.onButton1) 
    button2.Bind(wx.EVT_BUTTON, self.onButton2)     
#------------------------------------------------------------------------------
  def setClearValues(self):
    self.setValues('', 0, 0, 0, 0, '')
#------------------------------------------------------------------------------
  def setValues(self, title, distmin, distmax, hp, attitude, text):
    self.titletext = wx.TextCtrl(self.panel, wx.ID_ANY, title, pos = (150, 25), size=(240, -1))
    self.distmintext = wx.TextCtrl(self.panel, wx.ID_ANY, str(distmin), pos = (150, 60), size=(110, -1))
    self.distmaxtext = wx.TextCtrl(self.panel, wx.ID_ANY, str(distmax), pos = (280, 60), size=(110, -1))
    self.hptext = wx.TextCtrl(self.panel, wx.ID_ANY, str(hp), pos = (150, 95), size=(240, -1))
    self.attitudeidx = wx.ComboBox(self.panel, choices=Config.LANG.ATTITUDES, pos=(150, 130), size=(240, -1), style = wx.LB_SINGLE)
    self.attitudeidx.SetSelection(attitude)
    self.text = wx.TextCtrl(self.panel, wx.ID_ANY, text, pos = (10, 190), size=(380, 200), style= wx.TE_MULTILINE)
#------------------------------------------------------------------------------
  def onButton1(self, event):
    self.onOk = True
    self.Hide()
#------------------------------------------------------------------------------
  def onButton2(self, event):
    self.Hide()
#------------------------------------------------------------------------------
