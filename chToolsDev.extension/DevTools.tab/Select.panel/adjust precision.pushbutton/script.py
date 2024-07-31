# -*- coding: utf-8 -*-

__title__ = "Adjust precisision"
__doc__ =  """Change placement of the decimal place for the parameter ISY Mengde from millimeter to m
by other words it's moving the comma"""

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

param = 'ISY Mengde'

# -----------------Selection--------------------
selection_ids = uidoc.Selection.GetElementIds()
selected_elements =  [doc.GetElement(id) for id in selection_ids]


# -----------------Functions--------------------
def get_parameter(element,parameter_name):
    isy_param = element.LookupParameter(parameter_name).AsValueString()
    # param_length = len(isy_param)
    return isy_param

def change_unit_string(str):
    if len(str) < 4:
        new_str = str[:-3]+"0,"+str[-3:]
    else:
        new_str = str[:-3]+","+str[-3:]

    return new_str

def add_paramater(element, parameter_name):
    isy_param = get_parameter(element, parameter_name)
    
    if ';' in isy_param:
        isy_param = isy_param.split(';')
        for i in range(len(isy_param)):
            if i == 0:
                new_param = isy_param[i]
            elif i == len(isy_param)-1:
                new_param += ';' + isy_param[i-1]
            else:
                new_param += ';'+ isy_param[i]
    
    else: 
        new_param = isy_param
    return new_param

def set_parameter(element, parameter_name, value):
    isy_param = element.LookupParameter(parameter_name)
    isy_param.Set(value.ToString())
# ---------------------Filter--------------------


# ---------------------Logic--------------------

# for elem in selected_elements:
# #     param_value = get_parameter(elem, param)
# #     print(len(param_value), param_value,  change_unit_string(param_value))
#     add_paramater(elem, param)


# -------------------Transaction----------------------

t= Transaction(doc,__title__)
t.Start()

for sel_elem in selected_elements:
#     old_value = get_parameter(sel_elem, param)
    # set_parameter(sel_elem, param, change_unit_string(old_value))
    new_value = add_paramater(sel_elem, param)
    set_parameter(sel_elem, param, new_value)


t.Commit()