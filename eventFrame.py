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
class eventFrame(wx.Frame):
  panel = None
  tid = None
  tidtext = None
  titletext = None
  eventtext = None
  onOk = False
#------------------------------------------------------------------------------
  def __init__(self):
    super().__init__(None, title=Config.LANG.EVENT, size=(450, 470))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    button1 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.ROUND, (50, 50))
    button2 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.TURN, (135, 50))
    button3 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.SHIFT, (220, 50))
    button1.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(seconds=10): self.onButton1(event, timediff) )
    button2.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(minutes=15): self.onButton1(event, timediff) )
    button3.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(hours=6): self.onButton1(event, timediff) )
    lbl1 = wx.StaticText(self.panel, pos = (50, 100), size = (100,20), label = Config.LANG.TITLE)
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    lbl2 = wx.StaticText(self.panel, pos = (50, 160), size = (100,20), label = Config.LANG.EVENT)
    lbl2font = self.GetFont() 
    lbl2font.SetWeight(wx.BOLD)
    lbl2.SetFont(lbl2font)
    button4 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.OK, (130, 390))
    button5 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.CANCEL, (230, 390))
    button4.Bind(wx.EVT_BUTTON, self.onButton4) 
    button5.Bind(wx.EVT_BUTTON, self.onButton5) 
#------------------------------------------------------------------------------
  def setTime(self, tid):
    self.tid = tid
    self.printTime()
    self.titletext = wx.TextCtrl(self.panel, wx.ID_ANY, '', pos = (50, 120), size=(350, -1))
    self.eventtext = wx.TextCtrl(self.panel, wx.ID_ANY, '', pos = (50, 180), size=(350, 200), style= wx.TE_MULTILINE)
#------------------------------------------------------------------------------
  def setValues(self, tid, title, text):
    self.tid = tid
    self.printTime()
    self.titletext = wx.TextCtrl(self.panel, wx.ID_ANY, title, pos = (50, 120), size=(350, -1))
    self.eventtext = wx.TextCtrl(self.panel, wx.ID_ANY, text, pos = (50, 180), size=(350, 200), style= wx.TE_MULTILINE)
#------------------------------------------------------------------------------
  def onButton1(self, event, timediff):
    self.tid = self.tid + timediff
    self.printTime()
#------------------------------------------------------------------------------
  def onButton4(self, event):
    self.onOk = True
    self.Hide()
#------------------------------------------------------------------------------
  def onButton5(self, event):
    self.Hide()
#------------------------------------------------------------------------------
  def printTime(self):
    if not self.tidtext == None:
      self.tidtext.Destroy()
    dt = Config.LANG.WEEKDAY[self.tid.weekday()] + ' ' + Config.TIMEFORMAT
    self.tidtext = wx.StaticText(self.panel, pos = (50, 30), label = self.tid.strftime(dt))
#------------------------------------------------------------------------------
