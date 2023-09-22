# -*- coding: utf-8 -*-

__title__ = "Set coordinates by list"
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
#------------------Input------------------------
# Get selected elements
selection_ids = uidoc.Selection.GetElementIds()


# Get file
source_file = forms.pick_file(files_filter='*.csv|*.csv|''*.xml|*.xml|'
                                         '*.txt|*.txt|''All Files (*.*)|*.*', multi_file=True)
if source_file:
    print(source_file)  
       
if selection_ids:# Get coordinates of selection. For loop not need cause only one selection
    for selection_id in selection_ids:
        element = uidoc.Document.GetElement(selection_id)
        try:
            locPoint = element.Location.Point
            print(locPoint)
            mark = element.get_Parameter(BuiltInParameter.DOOR_NUMBER)
            mark = mark.AsValueString()
            print('Element id: {}, Mark = {}'.format(selection_id,mark))
            # print(mark)
        except:
            if element.Location.Curve:
                forms.alert('You must select a point based familys fx. Columns, Coordinate markers etc.', exitscript=True)
else:
    forms.alert('You must select minimym one point based familys fx. Columns, Coordinate markers etc.', exitscript=True)

# # Get coordinates 


# Xcor, Ycor, Zcor = userInput.split(',')
# Xcor = convert_to_internal_mm(float(Xcor))
# Ycor = convert_to_internal_mm(float(Ycor))
# Zcor = convert_to_internal_mm(float(Zcor))

# # -------------------Transaction----------------------
# # Sets coordinate of selection

# t= Transaction(doc,__title__)
# t.Start()

# newLocation = XYZ(Xcor, Ycor, Zcor)
# translation = newLocation - locPoint
# element.Location.Move(translation)

# t.Commit()

# ----------------End------------------.