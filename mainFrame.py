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
import json
import Config
from eventFrame import eventFrame
from Events import Events
#------------------------------------------------------------------------------
class mainFrame(wx.Frame):
  tid = None
  panel = None
  tidtext = None
  eventlist = {}
  events = []
#------------------------------------------------------------------------------
  def __init__(self, parent, title):
    super(mainFrame, self).__init__(parent, title=title, size=(1000, 500))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    self.tid = datetime.datetime.now()
    self.printTime()
    button1 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.ROUND, (50, 50))
    button2 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.TURN, (135, 50))
    button3 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.SHIFT, (220, 50))
    button4 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.SETTIME, (50, 20))
    button1.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(seconds=10): self.onButton1(event, timediff) )
    button2.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(minutes=15): self.onButton1(event, timediff) )
    button3.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(hours=6): self.onButton1(event, timediff) )
    button4.Bind(wx.EVT_BUTTON, self.onButton4)    
    lbl1 = wx.StaticText(self.panel, pos = (50, 100), label = Config.LANG.EVENTS + ' ')
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    self.eventlist = wx.ListBox(self.panel, size = (300,200), choices=[], pos=(50,120), style = wx.LB_SINGLE)
    self.eventlist.Bind(wx.EVT_LISTBOX_DCLICK, self.onDblClickListBox)
    button5 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.NEWEVENT, (50, 330))
    button6 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.DELEVENT, (160, 330))
    button5.Bind(wx.EVT_BUTTON, self.onButton5)  
    button6.Bind(wx.EVT_BUTTON, self.onButton6)  
    menubar = wx.MenuBar()
    menu1 = wx.Menu()
    menuitem1 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYOPEN, Config.LANG.MENYOPEN)
    self.Bind(wx.EVT_MENU, self.Load, menuitem1)    
    menuitem2 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYSAVE, Config.LANG.MENYSAVE)
    self.Bind(wx.EVT_MENU, self.Save, menuitem2)
    menuitem3 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYCONF, Config.LANG.MENYCONF)
    menuitem4 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYABOUT, Config.LANG.MENYABOUT)
    self.Bind(wx.EVT_MENU, self.About, menuitem4)
    menuitem5 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYQUIT, Config.LANG.MENYQUIT)
    self.Bind(wx.EVT_MENU, self.Quit, menuitem5)

    menubar.Append(menu1, Config.LANG.MENYTEXT)
    self.SetMenuBar(menubar)
#------------------------------------------------------------------------------
  def onButton1(self, event, timediff):
    self.tid = self.tid + timediff
    self.printTime()
#------------------------------------------------------------------------------
  def printTime(self):
    if not self.tidtext == None:
      self.tidtext.Destroy()
    self.tidtext = wx.StaticText(self.panel, pos = (140, 25), label = self.tid.strftime(Config.TIMEFORMATDAY))
    for idx, event in enumerate(self.events):
      if event.when <= self.tid:
        wx.MessageBox(event.text, event.title, style=wx.ICON_NONE)
        self.DeleteItem(idx)
#------------------------------------------------------------------------------
  def onButton4(self, event):
    dlg = wx.TextEntryDialog(self, Config.LANG.TIMEFORMATTITLE, Config.LANG.SETTIME)
    dlg.SetValue(self.tid.strftime(Config.TIMEFORMAT))
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
#------------------------------------------------------------------------------
  def Quit(self, event):
    exit(0)
#------------------------------------------------------------------------------
  def About(self, event):
    wx.MessageBox(Config.LANG.INFORMATION, Config.LANG.SOFTWARENAME, style=wx.ICON_NONE)
#------------------------------------------------------------------------------
  def Save(self, event):
    with wx.FileDialog(self, Config.LANG.MENYSAVE, wildcard="json files (*.json)|*.json",
        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
      if fileDialog.ShowModal() == wx.ID_CANCEL:
        return
      pathname = fileDialog.GetPath()
      if not '.json' in pathname:
        pathname = pathname + '.json'
      try:
        with open(pathname, 'w') as fp:
          fp.write(Config.JSONTIME % self.tid)
          for i in self.events:
            fp.write(json.dumps(i.__dict__, default=str))
        fp.close()
      except IOError:
        wx.LogError(Config.LANG.SAVEERROR % pathname)
#------------------------------------------------------------------------------
  def Load(self, event):
    with wx.FileDialog(self, Config.LANG.MENYSAVE, wildcard="json files (*.json)|*.json",
        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
      if fileDialog.ShowModal() == wx.ID_CANCEL:
        return
      pathname = fileDialog.GetPath()
      try:
        with open(pathname, 'r') as fp:
          data = json.load(fp)
        print(data)
        fp.close()
      except IOError:
        wx.LogError(Config.LANG.LOADERROR % pathname)
#------------------------------------------------------------------------------
