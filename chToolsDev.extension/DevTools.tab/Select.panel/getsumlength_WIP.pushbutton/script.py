# -*- coding: utf-8 -*-

__title__ = "GetSumLength_WIP"
__doc__ =  """Get the sum of the length of all selected elements"""

# -----------------Imports--------------------
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *

__author__ = "Casper Helmark"
__helpurl__ = "https://pyrevitlabs.notion.site/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0"

from pyrevit import revit

doc     = __revit__.ActiveUIDocument.Document
uidoc   = __revit__.ActiveUIDocument
app     = __revit__.Application

# -----------------Parameters--------------------

# ---------------------Filter--------------------

# Create an instance of the SelectionFilter class

# Create an instance of the ReferencePicker class
# -----------------Selection--------------------
picker = uidoc.Selection.PickObjects(ObjectType.Edge)
selected_elements =  [doc.GetElement(id) for id in picker]
# Show the reference picker dialog
# print(selected_elements)
# for i in picker:
#     print(i)

# Get the selected references


# # -----------------Functions--------------------

# def get_length(element):
#     edges = []
#     options = Options()
#     options.DetailLevel = ViewDetailLevel.Fine
#     elem_geom = element.get_Geometry(options)
#     for elem in elem_geom:
#         edges.append(elem)

    # length = edge.ApproximateLength().ToString()

    # return edge
# Iterate through the selected references
total_length = 0
for reference in picker:
    # Get the edge element from the reference
    # curve = oc.GetElement(reference)
    elem = doc.GetElement(reference)
    # edge_length = get_length(elem)
    options = Options()
    options.DetailLevel = ViewDetailLevel.Fine



    print(elem.get_Geometry(options))
    # Calculate the length of the edge
    # length = reference.ApproximateLength()

    # Add the length to the total
    # total_length += length

# Print the total length of the selected edges
# print("Total length of selected edges:", total_length)





# ---------------------Logic--------------------

# for elem in selected_elements:
#     param_value = get_parameter(elem, param)
#     print(len(param_value), param_value,  change_unit_string(param_value))

# -------------------Transaction----------------------

# t= Transaction(doc,__title__)
# t.Start()


# t.Commit()