# -*- coding: utf-8 -*-

__title__ = "Set coordinates"
__doc__ =  """Move the selected object to the specified coordinates"""

# -----------------Imports--------------------
from Autodesk.Revit.DB import *
import sys

__author__ = "Casper Helmark"
__helpurl__ = "https://pyrevitlabs.notion.site/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0"

from pyrevit import revit, forms
# from pyrevit.forms import WPFWindow

doc     = __revit__.ActiveUIDocument.Document
uidoc   = __revit__.ActiveUIDocument
app     = __revit__.Application

# -----------------Functions--------------------

def convert_to_internal_mm(length):
    length = UnitUtils.ConvertToInternalUnits(float(length), UnitTypeId.Millimeters)
    return length

# Get selected elements
selection_ids = uidoc.Selection.GetElementIds()

if len(selection_ids) > 1:
    forms.alert('You must only select one element', exitscript=True)

if len(selection_ids) == 0 :
    forms.alert('You must select one element to continue', exitscript=True)
   
       
for selection_id in selection_ids:
    # print(selection_id)

    # Get coordinates of selection
    element = uidoc.Document.GetElement(selection_id)
    locPoint = element.Location.Point
    # print(type(locPoint))

# Get coordinates userInputut
control = True
while control == True:

    userInput = forms.ask_for_string(default = 'X, Y, Z', prompt = "Coordinates in mm, where the object should be moved")

    try: 
        if  (',') not in userInput or 'X, Y, Z' in userInput:
            forms.alert('You must input coordinates in the format [X, Y, Z] to use this tool. Try Again', exitscript=False)
            control = True
        else:
            control = False
    except:
        sys.exit()

# Inserting Z=0 if Z's not given
if len(userInput.split(',')) < 3:
    userInput += ',0'
# Splits coordinates and converting to internals

Xcor, Ycor, Zcor = userInput.split(',')
Xcor = convert_to_internal_mm(float(Xcor))
Ycor = convert_to_internal_mm(float(Ycor))
Zcor = convert_to_internal_mm(float(Zcor))

# Sets coordinate of selection
# -------------------Transaction----------------------

t= Transaction(doc,__title__)
t.Start()

newLocation = XYZ(Xcor, Ycor, Zcor)
translation = newLocation - locPoint
element.Location.Move(translation)

t.Commit()