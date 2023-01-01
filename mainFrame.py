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
import random
import math
import decimal
import Config
from eventFrame import eventFrame
from Events import Events
from Characters import Characters
from charFrame import charFrame
#------------------------------------------------------------------------------
class mainFrame(wx.Frame):
  tid = None
  weatherstatus = None
  weathertime = None
  panel = None
  tidtext = None
  tidlabel = None
  eventlist = {}
  events = []
  characters = []
  charlist = {}
#------------------------------------------------------------------------------
  def __init__(self, parent, title):
    super(mainFrame, self).__init__(parent, title=title, size=(800, 600))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    menubar = wx.MenuBar()
    menu1 = wx.Menu()
    menuitem1 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYOPEN, Config.LANG.MENYOPEN)
    self.Bind(wx.EVT_MENU, self.Load, menuitem1)    
    menuitem2 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYSAVE, Config.LANG.MENYSAVE)
    self.Bind(wx.EVT_MENU, self.Save, menuitem2)
    #menuitem3 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYCONF, Config.LANG.MENYCONF)
    menuitem4 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYABOUT, Config.LANG.MENYABOUT)
    self.Bind(wx.EVT_MENU, self.About, menuitem4)
    menuitem5 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYQUIT, Config.LANG.MENYQUIT)
    self.Bind(wx.EVT_MENU, self.Quit, menuitem5)
    menubar.Append(menu1, Config.LANG.MENYTEXT)
    self.SetMenuBar(menubar)
    self.tid = datetime.datetime.now()
    self.weathertime = self.tid
    self.printTime()
    button4 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.SETTIME, (50, 110))
    button1 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.ROUND, (135, 110))
    button2 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.TURN, (220, 110))
    button3 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.SHIFT, (305, 110))
    button1.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(seconds=10): self.onButton1(event, timediff) )
    button2.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(minutes=15): self.onButton1(event, timediff) )
    button3.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(hours=6): self.onButton1(event, timediff) )
    button4.Bind(wx.EVT_BUTTON, self.onButton4)    
    lbl1 = wx.StaticText(self.panel, pos = (50, 150), size = (100,20), label = Config.LANG.EVENTS)
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    self.eventlist = wx.ListBox(self.panel, size = (355,300), choices=[], pos=(50,170), style = wx.LB_SINGLE)
    self.eventlist.Bind(wx.EVT_LISTBOX_DCLICK, self.onDblClickListBox)
    button5 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.NEWEVENT, (50, 480))
    button6 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.DELEVENT, (160, 480))
    button5.Bind(wx.EVT_BUTTON, self.onButton5)  
    button6.Bind(wx.EVT_BUTTON, self.onButton6)  
    lbl2 = wx.StaticText(self.panel, pos = (450, 30), size = (100,20), label = Config.LANG.CHARS)
    lbl2font = self.GetFont() 
    lbl2font.SetWeight(wx.BOLD)
    lbl2.SetFont(lbl2font)
    self.charlist = wx.ListBox(self.panel, size = (300,300), choices=[], pos=(450,50), style = wx.LB_SINGLE)
    self.charlist.Bind(wx.EVT_LISTBOX_DCLICK, self.onDblClickCharBox)
    button7 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.NEWCHAR, (450, 360))
    button8 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.DELCHAR, (560, 360))
    button7.Bind(wx.EVT_BUTTON, self.onButton7)  
    button8.Bind(wx.EVT_BUTTON, self.onButton8) 
#------------------------------------------------------------------------------
  def onButton1(self, event, timediff):
    self.tid = self.tid + timediff
    self.printTime()
#------------------------------------------------------------------------------
  def printTime(self):
    if not self.tidtext == None:
      self.tidtext.Destroy()
      self.tidlabel.Destroy()
    dt = Config.LANG.WEEKDAY[self.tid.weekday()] + ' ' + Config.DATEFORMAT
    self.tidlabel = wx.StaticText(self.panel, pos = (50, 25), size=(100, 50), label = Config.LANG.TIMETEXT)
    tidfont = self.GetFont() 
    tidfont.SetWeight(wx.BOLD)
    self.tidlabel.SetFont(tidfont)
    tidinfo = self.tid.strftime(dt) + '\n'
    dayphase = len(Config.DAYTIMELIMIT) - 1
    for idx, timelimit in enumerate(Config.DAYTIMELIMIT):
      if self.tid.time() > datetime.datetime.strptime(timelimit, '%H:%M').time():
        dayphase = idx
    tidinfo = tidinfo + Config.LANG.SUNTEXT[dayphase] + ' ' + self.tid.strftime(Config.TIMEFORMAT) + '\n'
    if self.weathertime <= self.tid:
      self.weathertime = self.weathertime + datetime.timedelta(hours=(random.randint(0,Config.WEATHERTIME)))
      r = random.random()
      self.weatherstatus = 0
      while r > Config.WEATHERRATIO[self.weatherstatus]:
        r = r - Config.WEATHERRATIO[self.weatherstatus]
        self.weatherstatus = self.weatherstatus + 1
    tidinfo = tidinfo + Config.LANG.WEATHER[self.weatherstatus] + '\n'
    for idx, event in enumerate(self.events):
      if event.when <= self.tid:
        wx.MessageBox(event.text, event.title, style=wx.ICON_NONE)
        self.DeleteEvent(idx)
    days = self.tid.day + self.tid.second / float(86400)
    phase = int((0.20439731 + float(days) * 0.03386319269) % 1 * float(8))
    tidinfo = tidinfo + Config.LANG.MOONPHASES[phase]
    self.tidtext = wx.StaticText(self.panel, pos = (150, 25), label = tidinfo)
#------------------------------------------------------------------------------
  def onButton4(self, event):
    dlg = wx.TextEntryDialog(self, Config.LANG.TIMEFORMATTITLE, Config.LANG.SETTIME)
    dlg.SetValue(self.tid.strftime(Config.TIMEFORMAT))
    if dlg.ShowModal() == wx.ID_OK:
      self.tid = datetime.datetime.strptime(dlg.GetValue(), Config.TIMEFORMAT)
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
    self.DeleteEvent(self.eventlist.GetSelection())
#------------------------------------------------------------------------------
  def onButton7(self, event):
    charframe = charFrame()
    charframe.setValues('', '', '', '')
    charframe.Show()
    while charframe.IsShown():
      wx.GetApp().Yield()
    if charframe.onOk:
      self.characters.append(Characters(charframe.nametext.GetValue(), int(charframe.actext.GetValue()), 
        int(charframe.wptext.GetValue()), charframe.chartext.GetValue()))
      self.charlist.Append(self.characters[self.charlist.GetCount()].name)
    charframe.Destroy()
#------------------------------------------------------------------------------
  def onButton8(self, event):
    if self.charlist.GetSelection()<0:
      return
    self.DeleteCharacter(self.charlist.GetSelection())
#------------------------------------------------------------------------------
  def DeleteEvent(self, itemn):  
    self.events.pop(itemn)
    self.eventlist.Delete(itemn)
#------------------------------------------------------------------------------
  def DeleteCharacter(self, itemn):  
    self.characters.pop(itemn)
    self.charlist.Delete(itemn)
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
  def onDblClickCharBox(self, event):
    if self.charlist.GetSelection()<0:
      return
    character = self.characters[self.charlist.GetSelection()]
    charframe = charFrame()
    charframe.setValues(character.name, character.ac, character.wp, character.text)
    charframe.Show()
    while charframe.IsShown():
      wx.GetApp().Yield()
    if charframe.onOk:
      character.name = charframe.nametext.GetValue()
      character.ac = int(charframe.actext.GetValue())
      character.wp = int(charframe.wptext.GetValue())
      character.text = charframe.chartext.GetValue()
      self.charlist.SetString(self.charlist.GetSelection(), self.characters[self.charlist.GetSelection()].name)
    charframe.Destroy()
#------------------------------------------------------------------------------
  def Quit(self, event):
    exit(0)
#------------------------------------------------------------------------------
  def About(self, event):
    wx.MessageBox(Config.LANG.INFORMATION, Config.SOFTWARENAME, style=wx.ICON_NONE)
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
          fp.write('{\n')
          fp.write(Config.JSONTIME % datetime.datetime.strftime(self.tid, '%Y-%m-%d %H:%M:%S'))
          fp.write(Config.JSONWEATHERINDEX % self.weatherstatus)
          fp.write(Config.JSONWEATHERTIME % datetime.datetime.strftime(self.weathertime, '%Y-%m-%d %H:%M:%S'))
          fp.write(Config.JSONEVENTS)
          for idx, i in enumerate(self.events):
            if idx > 0:
              fp.write(',\n')
            fp.write(Config.JSONEVENT % (i.when, i.title, i.text))
          fp.write('\n],\n' + Config.JSONCHARACTERS)
          for idx, i in enumerate(self.characters):
            if idx > 0:
              fp.write(',\n')
            fp.write(json.dumps(i.__dict__))
          fp.write('\n]\n}\n')
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
        fp.close()
        self.tid = datetime.datetime.strptime(data['time'], Config.DATETIMEFORMAT)
        self.weatherstatus = int(data['weatherindex'])
        self.weathertime = datetime.datetime.strptime(data['weathertime'], Config.DATETIMEFORMAT)
        self.printTime()
        self.events.clear()
        self.eventlist.Clear()
        for i in data['events']:
          self.events.append(Events(datetime.datetime.strptime(i['when'], Config.DATETIMEFORMAT), i['title'], i['text']))
          self.eventlist.Append(self.events[self.eventlist.GetCount()].title)
        for i in data['characters']:
          self.characters.append(Characters(i['name'], int(i['ac']), int(i['wp']), i['text']))
          self.charlist.Append(self.characters[self.charlist.GetCount()].name)
      except IOError:
        wx.LogError(Config.LANG.LOADERROR % pathname)
#------------------------------------------------------------------------------
