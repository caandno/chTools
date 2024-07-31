# -*- coding: utf-8 -*-
#! python3

__title__ = "Select model in place"
__doc__ =  """Select model in place object among selected object. Can be used to get and overview over how many model in place objects 
there is in the model"""

# -----------------Imports--------------------
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import ElementId, FilteredElementCollector, FamilyInstance
from Autodesk.Revit.UI.Selection import Selection, ObjectType, ISelectionFilter
from System.Collections.Generic import List


__author__ = "Casper Helmark"
__helpurl__ = "https://pyrevitlabs.notion.site/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0"

doc     = __revit__.ActiveUIDocument.Document
uidoc   = __revit__.ActiveUIDocument
app     = __revit__.Application
curview = doc.ActiveView

# -----------------Classes--------------------
class InPlaceFilter(ISelectionFilter):
    """
        The class inherits from ISelectionFilter and implements the AllowElement method to check if the given element is an instance of the FamilyInstance class and if its symbol's family is in place.
        
        Parameters:
            element (Any): The element to be checked.

        Returns:
            bool: True if the element is an instance of FamilyInstance and its symbol's family is in place, False otherwise.
    """
    def AllowElement(self, element):
        if isinstance(element, FamilyInstance):
            return element.Symbol.Family.IsInPlace
        return False
    
# -----------------Selection--------------------

selection = uidoc.Selection
selections = selection.PickElementsByRectangle(InPlaceFilter()) # Starts the picking process and filter out all elements that are not model in place

ids = List[ElementId](element.Id for element in selections) # Convert list of in place elements to list of element ids and converts to a ICollection List (from System.Collections.Generic import List)

selection.SetElementIds(ids)                    # Selects in place elements in the active view
# 