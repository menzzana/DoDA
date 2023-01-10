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
JSONENVIRONMENTSELECTED = '{\"title\": \"%s\", \"timeidx\": \"%s\", \"selected\": \"yes\", \"randomevents\": ['
JSONENVIRONMENTS = '\"environments\": [\n'
JSONENVIRONMENTIDX = '{\"idx\": \"%s\"}'
#------------------------------------------------------------------------------
class Environments:
  title = None
  timeidx = None
  randomeventidx = []
#------------------------------------------------------------------------------
  def __init__(self, title, timeidx, randomeventtitles):
    self.title = title
    self.timeidx = timeidx
    self.randomeventidx = randomeventtitles
#------------------------------------------------------------------------------
  def jsonSaveHeader():
    return JSONENVIRONMENTS
#------------------------------------------------------------------------------
  def jsonSave(self, selection, last):
    if last:
      ending = '\n]'
    else:
      ending = ',\n'
    if selection:
      data = JSONENVIRONMENTSELECTED % (self.title, self.timeidx)
    else:
      data = JSONENVIRONMENT % (self.title, self.timeidx)
    for idx, ev in enumerate(self.randomeventidx):
      data = data + JSONENVIRONMENTIDX % ev
      if idx < len(self.randomeventidx) - 1:
        data = data + ','
    if last:
      data = data + ']}\n'
    else:
      data = data + ']},\n'
    return data
#------------------------------------------------------------------------------
  @classmethod
  def jsonLoad(cls, data):
    eventidxs = []
    for i in data['randomevents']:
      if "title" in i:
        break
      eventidxs.append(int(i['idx']))
    return cls(data['title'], int(data['timeidx']), eventidxs)
#------------------------------------------------------------------------------
  @classmethod
  def jsonSelected(cls, data):
    return (True if "selected" in data else False)
#------------------------------------------------------------------------------
