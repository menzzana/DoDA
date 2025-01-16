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
class EventFrame(wx.Frame):
  panel = None
  tid = None
  tidtext = None
  titletext = None
  eventtext = None
  onOk = False
#------------------------------------------------------------------------------
  def __init__(self):
    super().__init__(None, title=Config.LANG.EVENT, size=(380, 470))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    self.panel.SetBackgroundColour(wx.Colour(230, 230, 255))
    button1 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.TIMES[0], pos = (10, 50), size = (90,-1))
    button2 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.TIMES[1], pos = (100, 50), size = (90,-1))
    button3 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.TIMES[2], pos = (190, 50), size = (90,-1))
    button4 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.TIMES[3], pos = (280, 50), size = (90,-1))
    button1.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(**Config.LANG.TIMEDIFF[0]): self.onButton1(event, timediff) )
    button2.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(**Config.LANG.TIMEDIFF[1]): self.onButton1(event, timediff) )
    button3.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(**Config.LANG.TIMEDIFF[2]): self.onButton1(event, timediff) )
    button4.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(**Config.LANG.TIMEDIFF[3]): self.onButton1(event, timediff) )
    lbl1 = wx.StaticText(self.panel, pos = (10, 100), size = (100,20), label = Config.LANG.TITLE)
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    lbl2 = wx.StaticText(self.panel, pos = (10, 160), size = (100,20), label = Config.LANG.EVENT)
    lbl2.SetFont(lbl1font)
    button5 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.OK, (30, 390))
    button6 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.CANCEL, (230, 390))
    button5.Bind(wx.EVT_BUTTON, self.onButton5) 
    button6.Bind(wx.EVT_BUTTON, self.onButton6) 
#------------------------------------------------------------------------------
  def setTime(self, tid):
    self.tid = tid
    self.printTime()
    self.titletext = wx.TextCtrl(self.panel, wx.ID_ANY, '', pos = (10, 120), size=(350, -1))
    self.eventtext = wx.TextCtrl(self.panel, wx.ID_ANY, '', pos = (10, 180), size=(350, 200), style= wx.TE_MULTILINE)
#------------------------------------------------------------------------------
  def setValues(self, tid, title, text):
    self.tid = tid
    self.printTime()
    self.titletext = wx.TextCtrl(self.panel, wx.ID_ANY, title, pos = (10, 120), size=(350, -1))
    self.eventtext = wx.TextCtrl(self.panel, wx.ID_ANY, text, pos = (10, 180), size=(350, 200), style= wx.TE_MULTILINE)
#------------------------------------------------------------------------------
  def onButton1(self, event, timediff):
    self.tid = self.tid + timediff
    self.printTime()
#------------------------------------------------------------------------------
  def onButton5(self, event):
    self.onOk = True
    self.Hide()
#------------------------------------------------------------------------------
  def onButton6(self, event):
    self.Hide()
#------------------------------------------------------------------------------
  def printTime(self):
    if not self.tidtext == None:
      self.tidtext.Destroy()
    dt = Config.LANG.WEEKDAY[self.tid.weekday()] + ' ' + Config.TIMEFORMAT
    self.tidtext = wx.StaticText(self.panel, pos = (10, 20), label = self.tid.strftime(dt))
#------------------------------------------------------------------------------
