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
JSONRANDOMEVENT = '{\"title\": \"%s\", \"distmin\": \"%s\", \"distmax\": \"%s\", \"hp\": \"%s\", \"attitude\": \"%s\", \"text\": \"%s\"}%s'
JSONRANDOMEVENTS = '\"randomevents\": [\n'
#------------------------------------------------------------------------------
class RandomEvents:
  title = None
  distmin = None
  distmax = None
  hp = None
  attitude = None
  text = None
#------------------------------------------------------------------------------
  def __init__(self, title, distmin, distmax, hp, attitude, text):
    self.title = title
    self.distmin = distmin
    self.distmax = distmax
    self.attitude = attitude
    self.hp = hp
    self.text = text
#------------------------------------------------------------------------------
  def jsonSaveHeader():
    return JSONRANDOMEVENTS
#------------------------------------------------------------------------------
  def jsonSave(self, last):
    if last:
      ending = '\n]'
    else:
      ending = ',\n'
    return JSONRANDOMEVENT % (self.title, self.distmin, self.distmax, self.hp, self.attitude, self.text, ending)
#------------------------------------------------------------------------------
  @classmethod
  def jsonLoad(cls, data):
    return cls(data['title'], int(data['distmin']), int(data['distmax']), int(data['hp']), int(data['attitude']), data['text'])
#------------------------------------------------------------------------------
