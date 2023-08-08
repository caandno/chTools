# -*- coding: utf-8 -*-

__title__ = "Copy name to comments"
__doc__ =  """Copy type name to comments"""

# -----------------Imports--------------------
from Autodesk.Revit.DB import *

__author__ = "Casper Helmark"
__helpurl__ = "https://pyrevitlabs.notion.site/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0"

from pyrevit import revit

doc     = __revit__.ActiveUIDocument.Document
uidoc   = __revit__.ActiveUIDocument
app     = __revit__.Application

# -----------------Selection--------------------
selection_ids = uidoc.Selection.GetElementIds()

# -----------------Functions--------------------
def copy_type_name_to_comments(elements):

    for element in elements:
        comment = element.get_Parameter(BuiltInParameter.ALL_MODEL_DESCRIPTION)
        print(comment)
        # element_type = element.Name
        # element_name = element_type[(element_type.find(':'))+1:]
        # comment.Set(element_name)

    print('familie typen {} har fået satt comments til {}'.format(element_type,element_name))

# ---------------------Filter--------------------
walls   = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()
columns = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType()
beams = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType()

# -------------------Transaction----------------------

# t= Transaction(doc,__title__)
# t.Start()


copy_type_name_to_comments(selection_ids)
# copy_type_name_to_comments(columns)
# copy_type_name_to_comments(beams)

# t.Commit()