# DoDA
## An Assistant for Dragonbane (Drakar och Demoner) roleplaying game

This is an assistant that can be used to play the role-playing game Drakar och Demoner,
named Dragonbane in english.

In order to run this assistant you need to
install the python package **wax**

See more information at https://www.wxpython.org/

## How to run

## Linux/Unix

You need to have python installed on your computer.
On Linux/Unix distribution this is oftenly default, but 
You also need wxPython for the GUI to work. Installation instructions
for this can be found at https://www.wxpython.org/pages/downloads/

For a swedish version just run **DoDA**
In case you want to run an english version, just run **DoDA_eng**

## Windows

You need to have python installed on your computer.
For windows you need to install python. See more documentation at https://www.python.org/downloads/windows/
* Download python via microsoft store
* Open command shell
* pip install -U wxPython

For a swedish version just run **DoDA_win**
In case you want to run an english version, just run **DoDA_win_eng**

## How to use

### Time

The software keeps track of time and changes it accordingly by pressing a button and set it, or by pressing
a button for round, quarter, shift.
The software also automatically checks if an events occur, and if an event has occured shows information
about the event and the deletes it.

### Events

Events are listed in set in the event list. Here you can add/delete events, as well as edit them by double-clicking
the event.
Events are defined by the time when the event occurs as well as title and information regarding it.

### Players

Players are recorded in the player list, where you can add information about the player, as well
as hitpoints, armor, willpower

The sum hitpoints of all players is then used for random encounter.

### Random events

You can add random events that are randomized on different time occasions.
Random events can either by monsters or just events.
Events are defined by not setting the hitpoint, aka it is by default set to 0.
For monsters instead you can add hitpoints, what their attitude is, the distance range  and some information.
Selecting that a random event should accur using the menu item, automatically selects a random event among
the ones that are currently selected in the list.

### Environments

You can add an environment in the drop-down box. An environment is caracterized by the place as well as the
time (Round, Quarter, Shift).
Also selecting an amount of random events will automatically save this selection in the selected environment.
If you change environment the selected random events will shift according. although no selected random events
will be selected when using No environment.
When progressing in time during the adventure a random event will be chosen depending on (Round, Quarter, Shift)
on the selected environment.
There is then a chance of 50% of a random event occuring.

### Configuration

There is no configuration per se in the software, but many parameters can be set by editing the
file *config.py*
 
