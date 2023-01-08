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
import Config
import EventFrame
import Events
import Characters
import CharacterFrame
import RandomEvents
import RandomEventFrame
import Environments
import EnvironmentFrame
#------------------------------------------------------------------------------
class MainFrame(wx.Frame):
  tid = None
  timeidx = 0
  weatherstatus = None
  weathertime = None
  panel = None
  tidtext = None
  randomev = None
  events = []
  eventlist = {}
  characters = []
  characterlist = {}
  environments = []
  environmentlist = {'None'}
  randomevents = []
  randomeventlist = {}
#------------------------------------------------------------------------------
  def __init__(self, parent, title):
    super(MainFrame, self).__init__(parent, title=title, size=(950, 600))
    self.Centre()
    self.panel = wx.Panel(self, wx.ID_ANY)
    self.panel.SetBackgroundColour(wx.Colour(230, 230, 255))
    menubar = wx.MenuBar()
    menu1 = wx.Menu()
    menuitem1 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYOPEN, Config.LANG.MENYOPEN)
    self.Bind(wx.EVT_MENU, self.Load, menuitem1)    
    menuitem2 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYSAVE, Config.LANG.MENYSAVE)
    self.Bind(wx.EVT_MENU, self.Save, menuitem2)
    #menuitem3 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYCONF, Config.LANG.MENYCONF)
    menuitem5 = menu1.Append(wx.ID_ANY, '&' + Config.LANG.MENYQUIT, Config.LANG.MENYQUIT)
    self.Bind(wx.EVT_MENU, self.Quit, menuitem5)
    menubar.Append(menu1, Config.LANG.MENYTEXT)
    menu2 = wx.Menu()
    menuitem6 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.SETTIME, Config.LANG.SETTIME)
    self.Bind(wx.EVT_MENU, self.setTime, menuitem6)
    menuitem7 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.NEWEVENT, Config.LANG.NEWEVENT)
    self.Bind(wx.EVT_MENU, self.newEvent, menuitem7)
    menuitem8 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.DELEVENT, Config.LANG.DELEVENT)
    self.Bind(wx.EVT_MENU, self.deleteEvent, menuitem8)
    menuitem9 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.NEWCHAR, Config.LANG.NEWCHAR)
    self.Bind(wx.EVT_MENU, self.newCharacter, menuitem9)
    menuitem10 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.DELCHAR, Config.LANG.DELCHAR)
    self.Bind(wx.EVT_MENU, self.deleteCharacter, menuitem10)
    menuitem11 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.NEWRANDOMEVENT, Config.LANG.NEWRANDOMEVENT)
    self.Bind(wx.EVT_MENU, self.newRandomEvent, menuitem11)
    menuitem12 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.DELRANDOMEVENT, Config.LANG.DELRANDOMEVENT)
    self.Bind(wx.EVT_MENU, self.deleteRandomEvent, menuitem12)
    menuitem13 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.NEWENVIRONMENT, Config.LANG.NEWENVIRONMENT)
    self.Bind(wx.EVT_MENU, self.newEnvironment, menuitem13)
    menuitem16 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.EDITENVIRONMENT, Config.LANG.DELENVIRONMENT)
    self.Bind(wx.EVT_MENU, self.editEnvironment, menuitem16)
    menuitem14 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.DELENVIRONMENT, Config.LANG.DELENVIRONMENT)
    self.Bind(wx.EVT_MENU, self.deleteEnvironment, menuitem14)
    menuitem15 = menu2.Append(wx.ID_ANY, '&' + Config.LANG.DORANDOMEVENT, Config.LANG.DORANDOMEVENT)
    self.Bind(wx.EVT_MENU, self.doRandomEventMenu, menuitem15)
    menubar.Append(menu2, Config.LANG.MENYEDIT)
    menu3 = wx.Menu()
    menuitem4 = menu3.Append(wx.ID_ANY, '&' + Config.LANG.MENYABOUT, Config.LANG.MENYABOUT)
    self.Bind(wx.EVT_MENU, self.About, menuitem4)
    menubar.Append(menu3, Config.LANG.MENYHELP)
    self.SetMenuBar(menubar)
    self.tid = datetime.datetime.now()
    self.weathertime = self.tid
    button1 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.ROUND, pos = (10, 90), size = (90,-1))
    button2 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.TURN, pos = (100, 90), size = (90,-1))
    button3 = wx.Button(self.panel, wx.ID_ANY, Config.LANG.SHIFT, pos = (190, 90), size = (90,-1))
    button1.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(seconds=10), timeidx = 0: self.onButton1(event, timediff, timeidx) )
    button2.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(minutes=15), timeidx = 1: self.onButton1(event, timediff, timeidx) )
    button3.Bind(wx.EVT_BUTTON, lambda event, timediff=datetime.timedelta(hours=6), timeidx = 2: self.onButton1(event, timediff, timeidx) )  
    lbl1 = wx.StaticText(self.panel, pos = (10, 150), size = (100,20), label = Config.LANG.EVENTS)
    lbl2 = wx.StaticText(self.panel, pos = (320, 150), size = (100,20), label = Config.LANG.CHARS)
    lbl3 = wx.StaticText(self.panel, pos = (10, 10), size=(50, 50), label = Config.LANG.TIMETEXT)
    lbl4 = wx.StaticText(self.panel, pos = (630, 150), size=(120, 50), label = Config.LANG.RANDOMEVENTTEXT)
    lbl5 = wx.StaticText(self.panel, pos = (630, 70), size=(120, 50), label = Config.LANG.ENVIRONMENTS)
    lbl1font = self.GetFont() 
    lbl1font.SetWeight(wx.BOLD)
    lbl1.SetFont(lbl1font)
    lbl2.SetFont(lbl1font)
    lbl3.SetFont(lbl1font)
    lbl4.SetFont(lbl1font)
    lbl5.SetFont(lbl1font)
    self.eventlist = wx.ListBox(self.panel, size = (300,360), choices=[], pos=(10,170), style = wx.LB_SINGLE)
    self.eventlist.Bind(wx.EVT_LISTBOX_DCLICK, self.onDblClickListBox)
    self.characterlist = wx.ListBox(self.panel, size = (300,360), choices=[], pos=(320,170), style = wx.LB_SINGLE)
    self.characterlist.Bind(wx.EVT_LISTBOX_DCLICK, self.onDblClickCharBox)
    self.environmentlist = wx.ComboBox(self.panel, size = (300, -1), choices=[], pos=(630,90), style = wx.LB_SINGLE)
    self.environmentlist.Append(Config.LANG.NONE)
    self.environmentlist.SetSelection(0)
    self.environmentlist.Bind(wx.EVT_COMBOBOX, self.onComboBoxChange)
    self.randomeventlist = wx.CheckListBox(self.panel, size = (300,360), choices=[], pos=(630,170), style = wx.LB_SINGLE)
    self.randomeventlist.Bind(wx.EVT_LISTBOX_DCLICK, self.onDblClickRandomEventBox)
    self.randomeventlist.Bind(wx.EVT_CHECKLISTBOX, self.onCheckRandomEventBox)
    self.printTime()
#------------------------------------------------------------------------------
  def onButton1(self, event, timediff, timeidx):
    self.tid = self.tid + timediff
    self.timeidx = timeidx
    self.printTime()
#------------------------------------------------------------------------------
  def printTime(self):
    if not self.tidtext == None:
      self.tidtext.Destroy()
    # Print time
    dt = Config.LANG.WEEKDAY[self.tid.weekday()] + ' ' + Config.DATEFORMAT
    tidinfo = self.tid.strftime(dt) + '\n'
    # Print phase of day
    dayphase = len(Config.DAYTIMELIMIT) - 1
    for idx, timelimit in enumerate(Config.DAYTIMELIMIT):
      if self.tid.time() > datetime.datetime.strptime(timelimit, '%H:%M').time():
        dayphase = idx
    tidinfo = tidinfo + Config.LANG.SUNTEXT[dayphase] + ' ' + self.tid.strftime(Config.TIMEFORMAT) + '\n'
    # Print weather
    if self.weathertime <= self.tid:
      self.weathertime = self.weathertime + datetime.timedelta(hours=(random.randint(0,Config.WEATHERTIME)))
      r = random.random()
      self.weatherstatus = 0
      while r > Config.WEATHERRATIO[self.weatherstatus]:
        r = r - Config.WEATHERRATIO[self.weatherstatus]
        self.weatherstatus = self.weatherstatus + 1
    tidinfo = tidinfo + Config.LANG.WEATHER[self.weatherstatus] + '\n'
    # Print moonphase
    days = self.tid.day + self.tid.second / float(86400)
    phase = int((0.20439731 + float(days) * 0.03386319269) % 1 * float(8))
    tidinfo = tidinfo + Config.LANG.MOONPHASES[phase]
    self.tidtext = wx.StaticText(self.panel, pos = (110, 10), label = tidinfo)
    self.checkEvents()
    if random.random() > Config.CHANCEENCOUNTER:
      if self.environmentlist.GetSelection() > 0:
        if self.timeidx == self.environments[self.environmentlist.GetSelection() - 1].timeidx:
          self.doRandomEvent()
#------------------------------------------------------------------------------
  def checkEvents(self):
    for idx, event in enumerate(self.events):
      if event.when <= self.tid:
        wx.MessageBox(event.text, event.title, style=wx.ICON_NONE)
        self.removeEvent(idx)
#------------------------------------------------------------------------------
  def setTime(self, event):
    dlg = wx.TextEntryDialog(self, Config.LANG.TIMEFORMATTITLE, Config.LANG.SETTIME)
    dlg.SetValue(self.tid.strftime(Config.TIMEFORMAT))
    if dlg.ShowModal() == wx.ID_OK:
      self.tid = datetime.datetime.strptime(dlg.GetValue(), Config.TIMEFORMAT)
      self.printTime()
    dlg.Destroy()
#------------------------------------------------------------------------------
  def newEvent(self, event):
    eventframe = EventFrame.EventFrame()
    eventframe.setTime(self.tid)
    eventframe.Show()
    while eventframe.IsShown():
      wx.GetApp().Yield()
    if eventframe.onOk:
      self.events.append(Events.Events(eventframe.tid, eventframe.titletext.GetValue(), eventframe.eventtext.GetValue()))
      self.eventlist.Append(self.events[self.eventlist.GetCount()].title)
    eventframe.Destroy()
#------------------------------------------------------------------------------
  def deleteEvent(self, event):
    if self.eventlist.GetSelection() < 0:
      return
    self.removeEvent(self.eventlist.GetSelection())
#------------------------------------------------------------------------------
  def removeEvent(self, itemn):
    self.events.pop(itemn)
    self.eventlist.Delete(itemn)
#------------------------------------------------------------------------------
  def newCharacter(self, event):
    charframe = CharacterFrame.CharacterFrame()
    charframe.setClearValues()
    charframe.Show()
    while charframe.IsShown():
      wx.GetApp().Yield()
    if charframe.onOk:
      self.characters.append(Characters.Characters(charframe.nametext.GetValue(), int(charframe.hptext.GetValue()), int(charframe.actext.GetValue()), 
        charframe.chartext.GetValue()))
      self.characterlist.Append(self.characters[self.characterlist.GetCount()].name)
    charframe.Destroy()
#------------------------------------------------------------------------------
  def deleteCharacter(self, event):
    if self.characterlist.GetSelection() < 0:
      return
    self.characters.pop(self.characterlist.GetSelection())
    self.characterlist.Delete(self.characterlist.GetSelection())
#------------------------------------------------------------------------------
  def doRandomEventMenu(self, event):
    self.doRandomEvent()
#------------------------------------------------------------------------------
  def doRandomEvent(self):
    if len(self.randomeventlist.GetCheckedItems()) <= 0:
      return
    idx = self.randomeventlist.GetCheckedItems()[random.randrange(0,len(self.randomeventlist.GetCheckedItems()))]
    if self.randomevents[idx].hp == 0:
      encountertext = Config.LANG.RANDOMEVENTENCOUNTERTEXT %  (self.randomevents[idx].title, self.randomevents[idx].text)
    else:
      if self.randomevents[idx].attitude > 0:
        attitude = Config.LANG.ATTITUDES[self.randomevents[idx].attitude]
      else:
        attitude = Config.LANG.ATTITUDES[random.randrange(1,len(Config.LANG.ATTITUDES))]
      numbers = int(sum(c.hp for c in self.characters)*random.random()*Config.HPRANGE/self.randomevents[idx].hp)
      if numbers == 0:
        numbers = 1
      encountertext = Config.LANG.ENCOUNTERTEXT %  (self.randomevents[idx].title,
        numbers,
        self.randomevents[idx].hp,
        random.randrange(self.randomevents[idx].distmin, self.randomevents[idx].distmax),
        attitude,
        Config.LANG.YES if random.random() > Config.DISCOVEREDENCOUNTER else Config.LANG.NO,
        self.randomevents[idx].text)
    wx.MessageBox(encountertext, Config.LANG.DORANDOMEVENT, style=wx.ICON_NONE)
#------------------------------------------------------------------------------
  def newEnvironment(self, event):
    environmentframe = EnvironmentFrame.EnvironmentFrame()
    environmentframe.setClearValues()
    environmentframe.Show()
    while environmentframe.IsShown():
      wx.GetApp().Yield()
    if environmentframe.onOk:
      self.environments.append(Environments.Environments(environmentframe.titletext.GetValue(), environmentframe.timeidx.GetSelection()))
      self.environmentlist.Append(environmentframe.titletext.GetValue())
    environmentframe.Destroy()
#------------------------------------------------------------------------------
  def newRandomEvent(self, event):
    randomeventframe = RandomEventFrame.RandomEventFrame()
    randomeventframe.setClearValues()
    randomeventframe.Show()
    while randomeventframe.IsShown():
      wx.GetApp().Yield()
    if randomeventframe.onOk:
      self.randomevents.append(RandomEvents.RandomEvents(randomeventframe.titletext.GetValue(),
        int(randomeventframe.distmintext.GetValue()),int(randomeventframe.distmaxtext.GetValue()),
        int(randomeventframe.hptext.GetValue()), randomeventframe.attitudeidx.GetSelection(), 
        randomeventframe.text.GetValue()))
      self.randomeventlist.Append(self.randomevents[self.randomeventlist.GetCount()].title)
    randomeventframe.Destroy()
#------------------------------------------------------------------------------
  def deleteRandomEvent(self, event):
    if self.randomeventlist.GetSelection() < 0:
      return
    for i in self.environments:
      if self.randomeventlist.GetSelection() in i.randomeventidx:
        i.randomeventidx.remove(self.randomeventlist.GetSelection())
      for idx,i2 in enumerate(i.randomeventidx):
        if i2 > self.randomeventlist.GetSelection():
          i.randomeventidx[idx] = i.randomeventidx[idx] - 1
    self.randomevents.pop(self.randomeventlist.GetSelection())
    self.randomeventlist.Delete(self.randomeventlist.GetSelection())
#------------------------------------------------------------------------------
  def deleteEnvironment(self, event):  
    if self.environmentlist.GetSelection() == 0:
      return
    self.environments.pop(self.environmentlist.GetSelection() - 1)
    self.environmentlist.Delete(self.environmentlist.GetSelection())
    self.environmentlist.SetSelection(0)
    self.removeEnvironmentSelection()
#------------------------------------------------------------------------------
  def onDblClickListBox(self, event):
    selection = self.eventlist.GetSelection()
    if selection < 0:
      return
    event = self.events[selection]
    eventframe = EventFrame.EventFrame()
    eventframe.setValues(event.when, event.title, event.text)
    eventframe.Show()
    while eventframe.IsShown():
      wx.GetApp().Yield()
    if eventframe.onOk:
      event.when = eventframe.tid
      event.title = eventframe.titletext.GetValue()
      event.text = eventframe.eventtext.GetValue()
      self.eventlist.SetString(selection, event.title)
    eventframe.Destroy()
#------------------------------------------------------------------------------
  def onDblClickCharBox(self, event):
    selection = self.characterlist.GetSelection()
    if selection < 0:
      return
    character = self.characters[selection]
    charframe = CharacterFrame.CharacterFrame()
    charframe.setValues(character.name, character.hp, character.ac, character.text)
    charframe.Show()
    while charframe.IsShown():
      wx.GetApp().Yield()
    if charframe.onOk:
      character.name = charframe.nametext.GetValue()
      character.hp = int(charframe.hptext.GetValue())
      character.ac = int(charframe.actext.GetValue())
      character.text = charframe.chartext.GetValue()
      self.characterlist.SetString(selection, character.name)
    charframe.Destroy()
#------------------------------------------------------------------------------
  def onDblClickRandomEventBox(self, event):
    selection = self.randomeventlist.GetSelection()
    if selection < 0:
      return
    randomevent = self.randomevents[selection]
    randomeventframe = RandomEventFrame.RandomEventFrame()
    randomeventframe.setValues(randomevent.title, randomevent.distmin, randomevent.distmax, randomevent.hp, randomevent.attitude, randomevent.text)
    randomeventframe.Show()
    while randomeventframe.IsShown():
      wx.GetApp().Yield()
    if randomeventframe.onOk:
      randomevent.title = randomeventframe.titletext.GetValue()
      randomevent.distmin = int(randomeventframe.distmintext.GetValue())
      randomevent.distmax = int(randomeventframe.distmaxtext.GetValue())
      randomevent.hp = int(randomeventframe.hptext.GetValue())
      randomevent.attitude = randomeventframe.attitudeidx.GetSelection()
      randomevent.text = randomeventframe.text.GetValue()
      self.randomeventlist.SetString(selection, randomevent.title)
    randomeventframe.Destroy()
#------------------------------------------------------------------------------
  def onCheckRandomEventBox(self, event):
    if self.environmentlist.GetSelection() == 0:
      return
    self.environments[self.environmentlist.GetSelection() - 1].randomeventidx.clear()
    idxs = []
    for i in self.randomeventlist.GetCheckedItems():
      idxs.append(i)
    self.environments[self.environmentlist.GetSelection() - 1].randomeventidx = idxs
#------------------------------------------------------------------------------
  def onComboBoxChange(self, event):
    for idx in range(self.randomeventlist.GetCount()):
      self.randomeventlist.Check(idx, False)
    if self.environmentlist.GetSelection() > 0:
      for i in self.environments[self.environmentlist.GetSelection() - 1].randomeventidx:
        self.randomeventlist.Check(i, True)
#------------------------------------------------------------------------------
  def editEnvironment(self, event):
    selection = self.environmentlist.GetSelection()
    if selection < 1:
      return
    environment = self.environments[selection - 1]
    environmentframe = EnvironmentFrame.EnvironmentFrame()
    environmentframe.setValues(environment.title, environment.timeidx)
    environmentframe.Show()
    while environmentframe.IsShown():
      wx.GetApp().Yield()
    if environmentframe.onOk:
      environment.title = environmentframe.titletext.GetValue()
      environment.timeidx = environmentframe.timeidx.GetSelection()
    environmentframe.Destroy()
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
          ncount = len(self.events)
          fp.write(Events.Events.jsonSaveHeader())
          for idx, i in enumerate(self.events):
            fp.write(i.jsonSave(idx == ncount - 1))
          ncount = len(self.characters)
          if ncount > 0:
            fp.write(',\n' + Characters.Characters.jsonSaveHeader())
            for idx, i in enumerate(self.characters):
              fp.write(i.jsonSave(idx == ncount - 1))
          ncount = len(self.randomevents)
          if ncount > 0:
            fp.write(',\n' + RandomEvents.RandomEvents.jsonSaveHeader())
            for idx, i in enumerate(self.randomevents):
              fp.write(i.jsonSave(idx == ncount - 1))
          ncount = len(self.environments)
          if ncount > 0:
            fp.write(',\n' + Environments.Environments.jsonSaveHeader())
            for idx, i in enumerate(self.environments):
              fp.write(i.jsonSave(idx == ncount - 1))
            fp.write(']')
          fp.write('}\n')
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
          self.events.append(Events.Events.jsonLoad(i))
          self.eventlist.Append(self.events[self.eventlist.GetCount()].title)
        self.characters.clear()
        self.characterlist.Clear()
        for i in data['characters']:
          self.characters.append(Characters.Characters.jsonLoad(i))
          self.characterlist.Append(self.characters[self.characterlist.GetCount()].name)
        self.randomevents.clear()
        self.randomeventlist.Clear()
        for i in data['randomevents']:
          self.randomevents.append(RandomEvents.RandomEvents.jsonLoad(i))
          self.randomeventlist.Append(self.randomevents[self.randomeventlist.GetCount()].title)
        self.environments.clear()
        self.environmentlist.Clear()
        self.environmentlist.Append(Config.LANG.NONE)
        self.environmentlist.SetSelection(0)
        for i in data['environments']:
          self.environments.append(Environments.Environments.jsonLoad(i))
          self.environmentlist.Append(self.environments[self.environmentlist.GetCount() - 1].title)
      except IOError:
        wx.LogError(Config.LANG.LOADERROR % pathname)
#------------------------------------------------------------------------------
