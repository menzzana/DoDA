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
JSONCHARACTER = '{\"name\": \"%s\", \"hp\": \"%s\", \"ac\": \"%s\", \"text\": \"%s\"}%s'
JSONCHARACTERS = '\"characters\": [\n'
#------------------------------------------------------------------------------
class Characters:
  name = None
  hp = None
  ac = None
  text = None
#------------------------------------------------------------------------------
  def __init__(self, name, hp, ac, text):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.text = text
#------------------------------------------------------------------------------
  def jsonSaveHeader():
    return JSONCHARACTERS
#------------------------------------------------------------------------------
  def jsonSave(self, last):
    if last:
      ending = '\n]'
    else:
      ending = ',\n'
    return JSONCHARACTER % (self.name, self.hp, self.ac, self.text, ending)
#------------------------------------------------------------------------------
  @classmethod
  def jsonLoad(cls, data):
    return cls(data['name'], int(data['hp']), int(data['ac']), data['text'])
#------------------------------------------------------------------------------


