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
import os
import sys
import Config
from MainFrame import MainFrame
#------------------------------------------------------------------------------
def main():
  Config.LANG = Config.Swedish()
  if len(sys.argv)>1:
    if sys.argv[1] == 'eng':
      Config.LANG = Config.English()
  Config.SOFTWARENAME = Config.SOFTWARENAME + "-" + os.popen(Config.LASTCOMMIT).read()
  app = wx.App()
  mainframe = MainFrame(None, Config.SOFTWARENAME)
  mainframe.Show()
  app.MainLoop()
#------------------------------------------------------------------------------
if __name__ == '__main__':  
  main()
#------------------------------------------------------------------------------
