#!/usr/bin/python
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
#==============================================================================
# Constants
#==============================================================================
VERSION = "0.1.0"
SOFTWARENAME = "DoDA v" + VERSION
ROUND = 'Runda'
TURN = 'Kvart'
SHIFT = 'Skift'
SETTIME = 'Ställ in'
EVENTS = 'Händelser'
NEWEVENT = 'Ny Händelse'
TIMEFORMAT = '%Y-%m-%d %H:%M:%S'
TIMEFORMATDAY = '%a '+TIMEFORMAT
TIMEFORMATTITLE = 'Tid (YYYY-MM-DD HH:MM:SS)'
DELEVENT = 'Ta bort händelse'
EVENT = 'Händelse'
OK = 'Ok'
CANCEL = 'Avbryt'
TITLE = 'Titel'
#==============================================================================
# mainFrame
#==============================================================================
class mainFrame(wx.Frame):
  tid = None
  panel = None
  tidtext = None
  eventlist = {}
  events = []
#------------------------------------------------------------------------------
  def __init__(self, parent):
    super(mainFrame, self).__init__(parent, title=SOFTWARENAME, size=(1000, 500))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    self.tid = datetime.datetime.now()
    self.printTime()
    button1 = wx.Button(self.panel, wx.ID_ANY, ROUND, (50, 50))
    button2 = wx.Button(self.panel, wx.ID_ANY, TURN, (135, 50))
    button3 = wx.Button(self.panel, wx.ID_ANY, SHIFT, (220, 50))
    button4 = wx.Button(self.panel, wx.ID_ANY, SETTIME, (50, 20))
    button1.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(seconds=10): self.onButton1(event, timediff) )
    button2.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(minutes=15): self.onButton1(event, timediff) )
    button3.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(hours=6): self.onButton1(event, timediff) )
    button4.Bind(wx.EVT_BUTTON, self.onButton4)    
    lbl1 = wx.StaticText(self.panel, pos = (50, 100), label = EVENTS + ' ')
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    self.eventlist = wx.ListBox(self.panel, size = (300,200), choices=[], pos=(50,120), style = wx.LB_SINGLE)
    self.eventlist.Bind(wx.EVT_LISTBOX_DCLICK, self.onDblClickListBox)
    button5 = wx.Button(self.panel, wx.ID_ANY, NEWEVENT, (50, 330))
    button6 = wx.Button(self.panel, wx.ID_ANY, DELEVENT, (160, 330))
    button5.Bind(wx.EVT_BUTTON, self.onButton5)  
    button6.Bind(wx.EVT_BUTTON, self.onButton6)  
#------------------------------------------------------------------------------
  def onButton1(self, event, timediff):
    self.tid = self.tid + timediff
    self.printTime()
#------------------------------------------------------------------------------
  def printTime(self):
    if not self.tidtext == None:
      self.tidtext.Destroy()
    self.tidtext = wx.StaticText(self.panel, pos = (140, 25), label = self.tid.strftime(TIMEFORMATDAY))
    for idx, event in enumerate(self.events):
      if event.when <= self.tid:
        wx.MessageBox(event.text, event.title, style=wx.ICON_NONE)
        self.DeleteItem(idx)
#------------------------------------------------------------------------------
  def onButton4(self, event):
    dlg = wx.TextEntryDialog(self, TIMEFORMATTITLE, SETTIME)
    dlg.SetValue(self.tid.strftime(TIMEFORMAT))
    if dlg.ShowModal() == wx.ID_OK:
      self.tid = datetime.datetime.strptime(dlg.GetValue(), TIMEFORMAT)
      self.printTime()
    dlg.Destroy()
#------------------------------------------------------------------------------
  def onButton5(self, event):
    eventframe = eventFrame()
    eventframe.setTime(self.tid)
    eventframe.Show()
    while eventframe.IsShown():
      wx.GetApp().Yield()
    if eventframe.onOk:
      self.events.append(Events(eventframe.tid, eventframe.titletext.GetValue(), eventframe.eventtext.GetValue()))
      self.eventlist.Append(self.events[self.eventlist.GetCount()].title)
    eventframe.Destroy()
#------------------------------------------------------------------------------
  def onButton6(self, event):
    if self.eventlist.GetSelection()<0:
      return
    self.DeleteItem(self.eventlist.GetSelection())
#------------------------------------------------------------------------------
  def DeleteItem(self, itemn):  
    self.events.pop(itemn)
    self.eventlist.Delete(itemn)
#------------------------------------------------------------------------------
  def onDblClickListBox(self, event):
    if self.eventlist.GetSelection()<0:
      return
    event = self.events[self.eventlist.GetSelection()]
    eventframe = eventFrame()
    eventframe.setValues(event.when, event.title, event.text)
    eventframe.Show()
    while eventframe.IsShown():
      wx.GetApp().Yield()
    if eventframe.onOk:
      event.when = eventframe.tid
      event.title = eventframe.titletext.GetValue()
      event.text = eventframe.eventtext.GetValue()
      self.eventlist.SetString(self.eventlist.GetSelection(), self.events[self.eventlist.GetSelection()].title)
    eventframe.Destroy()
#==============================================================================
class eventFrame(wx.Frame):
  panel = None
  tid = None
  tidtext = None
  titletext = None
  eventtext = None
  onOk = False
#------------------------------------------------------------------------------
  def __init__(self):
    super().__init__(None, title=EVENT, size=(450, 470))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    #self.tid = tid
    #self.printTime()
    button1 = wx.Button(self.panel, wx.ID_ANY, ROUND, (50, 50))
    button2 = wx.Button(self.panel, wx.ID_ANY, TURN, (135, 50))
    button3 = wx.Button(self.panel, wx.ID_ANY, SHIFT, (220, 50))
    button1.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(seconds=10): self.onButton1(event, timediff) )
    button2.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(minutes=15): self.onButton1(event, timediff) )
    button3.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(hours=6): self.onButton1(event, timediff) )
    lbl1 = wx.StaticText(self.panel, pos = (50, 100), label = TITLE + ' ')
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    lbl2 = wx.StaticText(self.panel, pos = (50, 160), label = EVENT + ' ')
    lbl2font = self.GetFont() 
    lbl2font.SetWeight(wx.BOLD)
    lbl2.SetFont(lbl2font)
    button4 = wx.Button(self.panel, wx.ID_ANY, OK, (130, 390))
    button5 = wx.Button(self.panel, wx.ID_ANY, CANCEL, (230, 390))
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
    self.tidtext = wx.StaticText(self.panel, pos = (50, 30), label = self.tid.strftime(TIMEFORMATDAY))
#==============================================================================
class Events:
  when = None
  title = None
  text = None
#------------------------------------------------------------------------------
  def __init__(self, when, title, text):
    self.when = when
    self.title = title
    self.text = text
#==============================================================================
# Main
#==============================================================================
def main():
  app = wx.App()
  mainframe = mainFrame(None)
  mainframe.Show()
  app.MainLoop()
#==============================================================================
if __name__ == '__main__':  
  main()
