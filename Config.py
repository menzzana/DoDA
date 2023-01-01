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
LANG = None
VERSION = "0.1.0"
SOFTWARENAME = "DoDA v" + VERSION
LASTCOMMIT = 'git log -n 1 --pretty=format:%h'
TIMEFORMAT = '%Y-%m-%d %H:%M:%S'
TIMEFORMATDAY = '%a '+TIMEFORMAT
JSONTIME = "{\"time\": \"%s\"}"
#------------------------------------------------------------------------------
class Swedish:
  ROUND = 'Runda'
  TURN = 'Kvart'
  SHIFT = 'Skift'
  SETTIME = 'Ställ in'
  EVENTS = 'Händelser'
  NEWEVENT = 'Ny Händelse'
  TIMEFORMATTITLE = 'Tid (YYYY-MM-DD HH:MM:SS)'
  DELEVENT = 'Ta bort händelse'
  EVENT = 'Händelse'
  OK = 'Ok'
  CANCEL = 'Avbryt'
  TITLE = 'Titel'
  MENYTEXT = '&Arkiv'
  MENYOPEN = 'Öppna'
  MENYSAVE = 'Spara'
  MENYCONF = 'Konfiguration'
  MENYQUIT = 'Avsluta'
  MENYABOUT = 'Om'
  INFORMATION = 'Drakar och Demoner Assistent.\nMer information finns på https://github.com/menzzana/DoDA.\nUtvecklad av Henric Zazzi'
  SAVEERROR = 'Kan inte spara till %s.'
  LOADERROR = 'Kan inte öppna %s.'
#------------------------------------------------------------------------------
class English:
  ROUND = 'Round'
  TURN = 'Turn'
  SHIFT = 'Shift'
  SETTIME = 'Set'
  EVENTS = 'Events'
  NEWEVENT = 'New Event'
  TIMEFORMATTITLE = 'Time (YYYY-MM-DD HH:MM:SS)'
  DELEVENT = 'Delete event'
  EVENT = 'Event'
  OK = 'Ok'
  CANCEL = 'Cancel'
  TITLE = 'Title'
  MENYTEXT = '&File'
  MENYOPEN = 'Open'
  MENYSAVE = 'Save'
  MENYCONF = 'Configuration'
  MENYQUIT = 'Quit'
  MENYABOUT = 'About'
  INFORMATION = 'Drakar och Demoner Assistant.\nMore information at https://github.com/menzzana/DoDA.\nDeveloped by Henric Zazzi'
  SAVEERROR = 'Cannot save to %s.'
  LOADERROR = 'Cannot open %s.'
#------------------------------------------------------------------------------
