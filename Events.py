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
import Config
import datetime
#------------------------------------------------------------------------------
JSONEVENT = '{\"when\": \"%s\", \"title\": \"%s\", \"text\": \"%s\"}%s'
JSONEVENTS = '\"events\": [\n'
#------------------------------------------------------------------------------
class Events:
  when = None
  title = None
  text = None
#------------------------------------------------------------------------------
  def __init__(self, when, title, text):
    self.when = when
    self.title = title
    self.text = text
#------------------------------------------------------------------------------
  def jsonSaveHeader():
    return JSONEVENTS
#------------------------------------------------------------------------------
  def jsonSave(self, last):
    if last:
      ending = '\n]'
    else:
      ending = ',\n'
    return JSONEVENT % (self.when, self.title, self.text, ending)
#------------------------------------------------------------------------------
  @classmethod
  def jsonLoad(cls, data):
    return cls(datetime.datetime.strptime(data['when'], Config.DATETIMEFORMAT), data['title'], data['text'])
#------------------------------------------------------------------------------
