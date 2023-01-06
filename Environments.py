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
JSONENVIRONMENT = '{\"title\": \"%s\", \"timeidx\": \"%s\", \"randomevents\": ['
JSONENVIRONMENTS = '\"environments\": [\n'
JSONENVIRONMENTTITLE = '{\"title\": \"%s\"}'
#------------------------------------------------------------------------------
class Environments:
  title = None
  timeidx = None
  randomeventtitles = []
#------------------------------------------------------------------------------
  def __init__(self, title, timeidx, randomeventtitles):
    self.title = title
    self.timeidx = timeidx
    self.randomeventtitles = randomeventtitles
#------------------------------------------------------------------------------
  def jsonSaveHeader():
    return JSONENVIRONMENTS
#------------------------------------------------------------------------------
  def jsonSave(self, last):
    if last:
      ending = '\n]'
    else:
      ending = ',\n'
    data = JSONENVIRONMENT % (self.title, self.timeidx)
    for idx, ev in enumerate(self.randomeventtitles):
      data = data + JSONENVIRONMENTTITLE % ev
      if idx < len(self.randomeventtitles) - 1:
        data = data + ','
    if last:
      data = data + ']}\n'
    else:
      data = data + ']},\n'
    return data
#------------------------------------------------------------------------------
  @classmethod
  def jsonLoad(cls, data):
    eventtitles = []
    for i in data['randomevents']:
      eventtitles.append(i['title'])
    return cls(data['title'], int(data['timeidx']), eventtitles)
#------------------------------------------------------------------------------
