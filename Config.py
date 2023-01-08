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
VERSION = "0.2.1"
SOFTWARENAME = "DoDA v" + VERSION
LASTCOMMIT = 'git log -n 1 --pretty=format:%h'
DATEFORMAT = '%Y-%m-%d'
TIMEFORMAT = '%H:%M:%S'
DATETIMEFORMAT = '%Y-%m-%d %H:%M:%S'
JSONTIME = '\"time\": \"%s\",\n'
JSONWEATHERINDEX = '\"weatherindex\": \"%s\",\n'
JSONWEATHERTIME = '\"weathertime\": \"%s\",\n'
MINUS = '-'
# Chance of one of the weathertypes occuring
WEATHERRATIO = [0.15,0.3,0.15,0.2,0.1,0.05,0.05]
# Weather shift happens every 0-WEATHETIME hours
WEATHERTIME = 6
# Sun variables
DAYTIMELIMIT = ['5:00', '7:00', '17:00', '19:00']
# Random encounter ratio
CHANCEENCOUNTER = 0.5
# Chance of discovery during encounter ratio
DISCOVEREDENCOUNTER = 0.5
# Ratio of hitpoint range for random monsters multiplied with party hp
HPRANGE = 1.2
#------------------------------------------------------------------------------
class Swedish:
  ROUND = 'Runda'
  TURN = 'Kvart'
  SHIFT = 'Skift'
  TIMES = [ROUND, TURN, SHIFT]
  FREQUENCY = 'Frekvens'
  SETTIME = 'Ställ in tid'
  EVENTS = 'Händelser'
  NEWEVENT = 'Ny Händelse'
  TIMEFORMATTITLE = 'Tid (YYYY-MM-DD HH:MM:SS)'
  DELEVENT = 'Ta bort händelse'
  EVENT = 'Händelse'
  CHARS = 'Spelare'
  NEWCHAR = 'Ny spelare'
  DELCHAR = 'Ta bort spelare'
  NAME = 'Namn'
  CHARHP = 'Kroppspoäng'
  CHARAC = 'Skyddsvärde'
  CHARWP = 'Kraftpoäng'
  CHARTEXT = 'Spelarinformation'
  OK = 'Ok'
  CANCEL = 'Avbryt'
  TITLE = 'Titel'
  MENYTEXT = '&Arkiv'
  MENYOPEN = 'Öppna'
  MENYSAVE = 'Spara'
  MENYCONF = 'Konfiguration'
  MENYQUIT = 'Avsluta'
  MENYHELP = 'Hjälp'
  MENYABOUT = 'Om'
  MENYEDIT = '&Redigera'
  INFORMATION = 'Drakar och Demoner Assistent.\nMer information finns på https://github.com/menzzana/DoDA.\nUtvecklad av Henric Zazzi'
  SAVEERROR = 'Kan inte spara till %s.'
  LOADERROR = 'Kan inte öppna %s.'
  WEEKDAY = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lördag', 'Söndag']
  WEATHER = ['Klart', 'Halvklart', 'Molnigt', 'Regn', 'Dimma', 'Storm', 'Åska']
  MOONPHASES = ['Nymåne', 'tilltagande halvmåne', 'Halvmåne', 'tilltagande fullmåne', 'Fullmåne', 'avtagande fullmåne', 'Halvmåne', 'avtagande halvmånen']
  TIMETEXT = 'Datum:\nTid:\nVäder:\nMånfas:'
  SUNTEXT = ['Soluppgång', 'Dag', 'Solnedgång', 'Natt']
  RANDOMEVENTTEXT = 'Slumphändelser'
  ENVIRONMENTS = 'Miljöer'
  NEWENVIRONMENT = 'Ny miljö'
  EDITENVIRONMENT = 'Redigera miljö'
  DELENVIRONMENT = 'Ta bort miljö'
  DORANDOMEVENT = 'Slumphändelse'
  NEWRANDOMEVENT = 'Ny slumphändelse'
  DELRANDOMEVENT = 'Ta bort slumphändelse'
  NONE = 'Ingen'
  DISTANCE = 'Avstånd'
  ATTITUDE = 'Attityd'
  ATTITUDES = ['Slump', 'Fientlig', 'Undvikande', 'Likgiltig', 'Vänlig']
  RANDOMEVENTENCOUNTERTEXT = 'Titel: %s\nHändelse\n%s\n'
  ENCOUNTERTEXT = 'Monster: %s\nAntal: %s\nKroppspoäng: %s\nAvstånd: %s\nAttityd: %s\nUpptäckt: %s\n\nInformation\n %s\n'
  YES = 'Ja'
  NO = 'Nej'
#------------------------------------------------------------------------------
class English:
  ROUND = 'Round'
  TURN = 'Stretch'
  SHIFT = 'Shift'
  TIMES = [ROUND, TURN, SHIFT]
  FREQUENCY = 'Frequency'
  SETTIME = 'Set time'
  EVENTS = 'Events'
  NEWEVENT = 'New Event'
  TIMEFORMATTITLE = 'Time (YYYY-MM-DD HH:MM:SS)'
  DELEVENT = 'Delete event'
  EVENT = 'Event'
  CHARS = 'Character'
  NEWCHAR = 'New character'
  DELCHAR = 'Delete character'
  NAME = 'Name'
  CHARHP = 'Hitpoints'
  CHARAC = 'Armor'
  CHARWP = 'Willpower'
  CHARTEXT = 'Playerinformation'
  OK = 'Ok'
  CANCEL = 'Cancel'
  TITLE = 'Title'
  MENYTEXT = '&File'
  MENYOPEN = 'Open'
  MENYSAVE = 'Save'
  MENYCONF = 'Configuration'
  MENYQUIT = 'Quit'
  MENYABOUT = 'About'
  MENYHELP = 'Help'
  MENYEDIT = '&Edit'
  INFORMATION = 'Dragonbane Assistant.\nMore information at https://github.com/menzzana/DoDA.\nDeveloped by Henric Zazzi'
  SAVEERROR = 'Cannot save to %s.'
  LOADERROR = 'Cannot open %s.'
  WEEKDAY = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  WEATHER = ['Clear', 'Partially cloudy', 'Cloudy', 'Rain', 'Fog', 'Storm', 'Thunderstorm']
  MOONPHASES = ['New Moon', 'Waxing Crescent', 'First Quarter', 'Waxing Gibbous', 'Full Moon', 'Waning Gibbous', 'Last Quarter', 'Waning Crescent']
  TIMETEXT = 'Date:\nTime:\nWeather:\nMoonphase:'
  SUNTEXT = ['Dawn', 'Day', 'Dusk', 'Night']
  RANDOMEVENTTEXT = 'Random events'
  ENVIRONMENTS = 'Environments'
  NEWENVIRONMENT = 'New environment'
  EDITENVIRONMENT = 'Edit environment'
  DELENVIRONMENT = 'Delete environment'
  DORANDOMEVENT = 'Random event'
  NEWRANDOMEVENT = 'New random event'
  DELRANDOMEVENT = 'Delete random event'
  NONE = 'None'
  DISTANCE = 'Distance'
  ATTITUDE = 'Attitude'
  ATTITUDES = ['Random', 'Hostile', 'Avoidant', 'Indifferent', 'Friendly']
  RANDOMEVENTENCOUNTERTEXT = 'Title: %s\nEvent\n %s\n'
  ENCOUNTERTEXT = 'Monster: %s\nNumbers: %s\nHitpoints: %s\nDistance: %s\nAttitude: %s\nDiscovered: %s\n\nInformation\n%s\n'
  YES = 'Yes'
  NO = 'No'
#------------------------------------------------------------------------------
