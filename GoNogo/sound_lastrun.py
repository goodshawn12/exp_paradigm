#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on October 15, 2019, at 18:54
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'sound'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\goods\\OneDrive\\Desktop\\Experiments\\GoNogo\\sound_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruc1"
instruc1Clock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text='Instruction: \n\nIn the experiment, you will hear two tones in sequence.\n\nIf the two tones have the same pitch,\nuse your right hand to press the SPACE bar.\n\nIf the two tones have different pitches,\nno action needed.\n\nWhen you are ready,\nPress any key to continue. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruc2"
instruc2Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Here is an example of low frequency tone.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sound_7 = sound.Sound('1000', secs=0.1, stereo=True)
sound_7.setVolume(0.75)
text_7 = visual.TextStim(win=win, name='text_7',
    text='Here is an example of high frequency tone.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sound_2 = sound.Sound('1300', secs=0.1, stereo=True)
sound_2.setVolume(0.75)
text_9 = visual.TextStim(win=win, name='text_9',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "instruc3"
instruc3Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Practice session\n\nPress any key to start',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruc4"
instruc4Clock = core.Clock()
sound_3 = sound.Sound('1000', secs=0.1, stereo=True)
sound_3.setVolume(0.75)
text_6 = visual.TextStim(win=win, name='text_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
sound_4 = sound.Sound('A', secs=0.1, stereo=True)
sound_4.setVolume(0.75)
text_10 = visual.TextStim(win=win, name='text_10',
    text="Two tones are different. \n\nDon't press any key!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
sound_5 = sound.Sound('1000', secs=0.1, stereo=True)
sound_5.setVolume(0.75)
text_13 = visual.TextStim(win=win, name='text_13',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
sound_8 = sound.Sound('1000', secs=0.1, stereo=True)
sound_8.setVolume(0.75)
text_14 = visual.TextStim(win=win, name='text_14',
    text='Two tones are the same!\n\nPress SPACE this time!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "instruc5"
instruc5Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Experiment session:\n\nWhen you are ready,\nPress any key to start!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "L"
LClock = core.Clock()
low = sound.Sound('1000', secs=0.1, stereo=True)
low.setVolume(0.75)
sound_6 = sound.Sound('A', secs=0.1, stereo=True)
sound_6.setVolume(0.75)
text_11 = visual.TextStim(win=win, name='text_11',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "routine"
routineClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruc1"-------
t = 0
instruc1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = keyboard.Keyboard()
# keep track of which components have finished
instruc1Components = [instruction, key_resp_2]
for thisComponent in instruc1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruc1"-------
while continueRoutine:
    # get current time
    t = instruc1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if t >= 0.0 and instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction.tStart = t  # not accounting for scr refresh
        instruction.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # not accounting for scr refresh
        key_resp_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruc1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruc1"-------
for thisComponent in instruc1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction.started', instruction.tStartRefresh)
thisExp.addData('instruction.stopped', instruction.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruc1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruc2"-------
t = 0
instruc2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(7.500000)
# update component parameters for each repeat
sound_7.setSound('1000', secs=0.1)
sound_7.setVolume(0.75, log=False)
sound_2.setSound('1300', secs=0.1)
sound_2.setVolume(0.75, log=False)
# keep track of which components have finished
instruc2Components = [text_12, sound_7, text_7, sound_2, text_9]
for thisComponent in instruc2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruc2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instruc2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t  # not accounting for scr refresh
        text_12.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_12.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_12.tStop = t  # not accounting for scr refresh
        text_12.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
        text_12.setAutoDraw(False)
    # start/stop sound_7
    if t >= 2 and sound_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_7.tStart = t  # not accounting for scr refresh
        sound_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_7, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_7.play)  # screen flip
    frameRemains = 2 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_7.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_7.tStop = t  # not accounting for scr refresh
        sound_7.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_7, 'tStopRefresh')  # time at next scr refresh
        if 0.1 > 0.5:  # don't force-stop brief sounds
            sound_7.stop()
    
    # *text_7* updates
    if t >= 3.5 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # not accounting for scr refresh
        text_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    frameRemains = 3.5 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_7.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_7.tStop = t  # not accounting for scr refresh
        text_7.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
        text_7.setAutoDraw(False)
    # start/stop sound_2
    if t >= 5.5 and sound_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_2.tStart = t  # not accounting for scr refresh
        sound_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_2, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_2.play)  # screen flip
    frameRemains = 5.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_2.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_2.tStop = t  # not accounting for scr refresh
        sound_2.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
        if 0.1 > 0.5:  # don't force-stop brief sounds
            sound_2.stop()
    
    # *text_9* updates
    if t >= 6.5 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # not accounting for scr refresh
        text_9.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    frameRemains = 6.5 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_9.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_9.tStop = t  # not accounting for scr refresh
        text_9.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
        text_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruc2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruc2"-------
for thisComponent in instruc2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
sound_7.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_7.started', sound_7.tStartRefresh)
thisExp.addData('sound_7.stopped', sound_7.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
sound_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_2.started', sound_2.tStartRefresh)
thisExp.addData('sound_2.stopped', sound_2.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)

# ------Prepare to start Routine "instruc3"-------
t = 0
instruc3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = keyboard.Keyboard()
# keep track of which components have finished
instruc3Components = [text_5, key_resp_4]
for thisComponent in instruc3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruc3"-------
while continueRoutine:
    # get current time
    t = instruc3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # not accounting for scr refresh
        text_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # not accounting for scr refresh
        key_resp_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        key_resp_4.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = key_resp_4.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_4.keys = theseKeys.name  # just the last key pressed
            key_resp_4.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruc3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruc3"-------
for thisComponent in instruc3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruc3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruc4"-------
t = 0
instruc4Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
sound_3.setSound('1000', secs=0.1)
sound_3.setVolume(0.75, log=False)
sound_4.setSound('1300', secs=0.1)
sound_4.setVolume(0.75, log=False)
sound_5.setSound('1000', secs=0.1)
sound_5.setVolume(0.75, log=False)
sound_8.setSound('1000', secs=0.1)
sound_8.setVolume(0.75, log=False)
# keep track of which components have finished
instruc4Components = [sound_3, text_6, sound_4, text_10, sound_5, text_13, sound_8, text_14]
for thisComponent in instruc4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruc4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instruc4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_3
    if t >= 0.0 and sound_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_3.tStart = t  # not accounting for scr refresh
        sound_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_3, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_3.play)  # screen flip
    frameRemains = 0.0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_3.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_3.tStop = t  # not accounting for scr refresh
        sound_3.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
        if 0.1 > 0.5:  # don't force-stop brief sounds
            sound_3.stop()
    
    # *text_6* updates
    if t >= 0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # not accounting for scr refresh
        text_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    frameRemains = 0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_6.tStop = t  # not accounting for scr refresh
        text_6.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
        text_6.setAutoDraw(False)
    # start/stop sound_4
    if t >= 0.9 and sound_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_4.tStart = t  # not accounting for scr refresh
        sound_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_4, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_4.play)  # screen flip
    frameRemains = 0.9 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_4.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_4.tStop = t  # not accounting for scr refresh
        sound_4.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_4, 'tStopRefresh')  # time at next scr refresh
        if 0.1 > 0.5:  # don't force-stop brief sounds
            sound_4.stop()
    
    # *text_10* updates
    if t >= 1.5 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # not accounting for scr refresh
        text_10.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    frameRemains = 1.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_10.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_10.tStop = t  # not accounting for scr refresh
        text_10.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
        text_10.setAutoDraw(False)
    # start/stop sound_5
    if t >= 3.5 and sound_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_5.tStart = t  # not accounting for scr refresh
        sound_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_5, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_5.play)  # screen flip
    frameRemains = 3.5 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_5.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_5.tStop = t  # not accounting for scr refresh
        sound_5.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_5, 'tStopRefresh')  # time at next scr refresh
        if 0.1 > 0.5:  # don't force-stop brief sounds
            sound_5.stop()
    
    # *text_13* updates
    if t >= 3.5 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t  # not accounting for scr refresh
        text_13.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    frameRemains = 3.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_13.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_13.tStop = t  # not accounting for scr refresh
        text_13.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
        text_13.setAutoDraw(False)
    # start/stop sound_8
    if t >= 4.4 and sound_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_8.tStart = t  # not accounting for scr refresh
        sound_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_8, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_8.play)  # screen flip
    frameRemains = 4.4 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_8.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_8.tStop = t  # not accounting for scr refresh
        sound_8.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
        if 0.1 > 0.5:  # don't force-stop brief sounds
            sound_8.stop()
    
    # *text_14* updates
    if t >= 5 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t  # not accounting for scr refresh
        text_14.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    frameRemains = 5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_14.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_14.tStop = t  # not accounting for scr refresh
        text_14.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
        text_14.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruc4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruc4"-------
for thisComponent in instruc4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_3.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_3.started', sound_3.tStartRefresh)
thisExp.addData('sound_3.stopped', sound_3.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
sound_4.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_4.started', sound_4.tStartRefresh)
thisExp.addData('sound_4.stopped', sound_4.tStopRefresh)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
sound_5.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_5.started', sound_5.tStartRefresh)
thisExp.addData('sound_5.stopped', sound_5.tStopRefresh)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
sound_8.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_8.started', sound_8.tStartRefresh)
thisExp.addData('sound_8.stopped', sound_8.tStopRefresh)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)

# ------Prepare to start Routine "instruc5"-------
t = 0
instruc5Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = keyboard.Keyboard()
# keep track of which components have finished
instruc5Components = [text_8, key_resp_6]
for thisComponent in instruc5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruc5"-------
while continueRoutine:
    # get current time
    t = instruc5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if t >= 0.5 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # not accounting for scr refresh
        text_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.5 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # not accounting for scr refresh
        key_resp_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        key_resp_6.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = key_resp_6.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruc5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruc5"-------
for thisComponent in instruc5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruc5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loopcount.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=4, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('frequency.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "L"-------
        t = 0
        LClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        low.setSound('1000', secs=0.1)
        low.setVolume(0.75, log=False)
        sound_6.setSound(fre, secs=0.1)
        sound_6.setVolume(0.75, log=False)
        key_resp_9 = keyboard.Keyboard()
        # keep track of which components have finished
        LComponents = [low, sound_6, key_resp_9, text_11]
        for thisComponent in LComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "L"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = LClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop low
            if t >= 0 and low.status == NOT_STARTED:
                # keep track of start time/frame for later
                low.tStart = t  # not accounting for scr refresh
                low.frameNStart = frameN  # exact frame index
                win.timeOnFlip(low, 'tStartRefresh')  # time at next scr refresh
                win.callOnFlip(low.play)  # screen flip
            frameRemains = 0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if low.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                low.tStop = t  # not accounting for scr refresh
                low.frameNStop = frameN  # exact frame index
                win.timeOnFlip(low, 'tStopRefresh')  # time at next scr refresh
                if 0.1 > 0.5:  # don't force-stop brief sounds
                    low.stop()
            # start/stop sound_6
            if t >= 0.9 and sound_6.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_6.tStart = t  # not accounting for scr refresh
                sound_6.frameNStart = frameN  # exact frame index
                win.timeOnFlip(sound_6, 'tStartRefresh')  # time at next scr refresh
                win.callOnFlip(sound_6.play)  # screen flip
            frameRemains = 0.9 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if sound_6.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                sound_6.tStop = t  # not accounting for scr refresh
                sound_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_6, 'tStopRefresh')  # time at next scr refresh
                if 0.1 > 0.5:  # don't force-stop brief sounds
                    sound_6.stop()
            
            # *key_resp_9* updates
            if t >= 0.9 and key_resp_9.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_9.tStart = t  # not accounting for scr refresh
                key_resp_9.frameNStart = frameN  # exact frame index
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                key_resp_9.clearEvents(eventType='keyboard')
            frameRemains = 0.9 + 1.6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_9.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                key_resp_9.tStop = t  # not accounting for scr refresh
                key_resp_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_9, 'tStopRefresh')  # time at next scr refresh
                key_resp_9.status = FINISHED
            if key_resp_9.status == STARTED:
                theseKeys = key_resp_9.getKeys(keyList=['Enter'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    key_resp_9.keys = theseKeys.name  # just the last key pressed
                    key_resp_9.rt = theseKeys.rt
            
            # *text_11* updates
            if t >= 0.0 and text_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_11.tStart = t  # not accounting for scr refresh
                text_11.frameNStart = frameN  # exact frame index
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                text_11.setAutoDraw(True)
            frameRemains = 0.0 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_11.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                text_11.tStop = t  # not accounting for scr refresh
                text_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                text_11.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "L"-------
        for thisComponent in LComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        low.stop()  # ensure sound has stopped at end of routine
        trials.addData('low.started', low.tStartRefresh)
        trials.addData('low.stopped', low.tStopRefresh)
        sound_6.stop()  # ensure sound has stopped at end of routine
        trials.addData('sound_6.started', sound_6.tStartRefresh)
        trials.addData('sound_6.stopped', sound_6.tStopRefresh)
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys = None
        trials.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            trials.addData('key_resp_9.rt', key_resp_9.rt)
        trials.addData('key_resp_9.started', key_resp_9.tStartRefresh)
        trials.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
        trials.addData('text_11.started', text_11.tStartRefresh)
        trials.addData('text_11.stopped', text_11.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 4 repeats of 'trials'
    
    
    # ------Prepare to start Routine "routine"-------
    t = 0
    routineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    text.setText(count
)
    key_resp_3 = keyboard.Keyboard()
    # keep track of which components have finished
    routineComponents = [text, key_resp_3]
    for thisComponent in routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # not accounting for scr refresh
            text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        frameRemains = 0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
        
        # *key_resp_3* updates
        if t >= 0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # not accounting for scr refresh
            key_resp_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            key_resp_3.clearEvents(eventType='keyboard')
        frameRemains = 0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_3.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp_3.tStop = t  # not accounting for scr refresh
            key_resp_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
            key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_3.keys = theseKeys.name  # just the last key pressed
                key_resp_3.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine"-------
    for thisComponent in routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text.started', text.tStartRefresh)
    trials_2.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_2.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_2.addData('key_resp_3.rt', key_resp_3.rt)
    trials_2.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials_2.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.5 repeats of 'trials_2'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
