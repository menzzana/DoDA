# DoDA
## An Assistant for Dragonbane (Drakar och Demoner) and Dungeon&Dragons roleplaying game

This is an assistant that can be used to play the role-playing game Drakar och Demoner,
named Dragonbane in english, and Dungeon&Dragons

![](https://user-images.githubusercontent.com/6664679/224726545-ea8e9444-1776-4867-b584-f44940959806.jpg)

In order to run this assistant you need to
install the python package **wax**

See more information at https://www.wxpython.org/

## How to run

## Linux/Unix

You need to have python installed on your computer.
On Linux/Unix distribution this is oftenly default, but 
You also need wxPython for the GUI to work. Installation instructions
for this can be found at https://www.wxpython.org/pages/downloads/

By default this software primarily targets Drakar och Demoner.
For a swedish version just run **DoDA**
In case you want to run an english version, just run **DoDA_eng**
In case you want to run an Dungeon&Dragons version, just run **DoDA_dnd**

## Windows

You need to have python installed on your computer.
For windows you need to install python. See more documentation at https://www.python.org/downloads/windows/
* Download python via microsoft store
* Open command shell
* pip install -U wxPython

For a swedish version just run **DoDA_win**
In case you want to run an english version, just run **DoDA_win_eng**
In case you want to run an english version, just run **DoDA_win_dnd**

## MAC(OSX)

* Install Python via the terminal
  * Installera attrdict3 using *pip install attrdict3*
  * Installera wxPython using *pip install wxPython*
* Should be able to start the program by double-clicking **DoDA_mac**, **DoDA_mac_eng** or **DoDA_mac_dnd** as well
* Otherwise start program by double-clicking on **DoDA.py**, then click **Run** -> **Run Module**



## How to use

### Time

The software keeps track of time and changes it accordingly by pressing a button and set it, or by pressing
a button for the different time increases.
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
Events are defined by not setting the hitpoint/HP, aka it is by default set to 0.
For monsters instead you can add hitpoints, what their attitude is, the distance range  and some information.
Selecting that a random event should accur using the menu item, automatically selects a random event among
the ones that are currently selected in the list.

### Environments

You can add an environment in the drop-down box. An environment is caracterized by the place as well as the
time.
Also selecting an amount of random events will automatically save this selection in the selected environment.
If you change environment the selected random events will shift according. although no selected random events
will be selected when using No environment.
When progressing in time during the adventure a random event will be chosen depending on the time settings
on the selected environment.

## Configuration

There is no configuration per se in the software, but many parameters can be set by editing the
file *config.py*

### Weather

The variable **WEATHERRATIO** is a list of ratios for
different weather situations. You can examine the **WEATHER** variable
to see which ones are connected to each value. The sum of the values is 1.

### Encounters

The variable **CHANCEENCOUNTER** describes the ratio for a random encounter happening.
By default this is set to 0.2 aka 20% chance of having a random encounter in a given selected
timeframe for the environment.

### Risk of being discovered

The variable **DISCOVEREDENCOUNTER** describes the ratio for being discovered during a random encounter happening.
By default this is set to 0.4 aka 40% chance of being discovered.

### Strength of wandering monsters

The variable **HPRANGE** describes the strength of the wandering monster party.
Each monster has a specific hitpoints which also the character have.
The number of monsters facing the characters is equal to the sum of the hitpoints for
the party divided by the monsters hitpoints multiplied by **HPRANGE**.

[Number of monsters]=[Sum Party HP]*HPRANGE/[Monster HP]
