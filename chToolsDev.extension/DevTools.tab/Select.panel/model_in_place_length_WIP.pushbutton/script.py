# -*- coding: utf-8 -*-
#! python3

__title__ = "model_in_place_length_WIP"
__doc__ =  """Calculate the length of a model in place family and writes it to a length parameter"""

# -----------------Imports--------------------
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, FamilyInstance, \
        Options, Edge, Solid, GeometryInstance, ViewDetailLevel, UnitUtils, UnitTypeId,\
        Element,Parameter, Transaction, XYZ
from Autodesk.Revit.UI.Selection import ObjectType, Selection
clr.AddReference('RevitAPIUI')
# from Autodesk.Revit.UI import *

__author__ = "Casper Helmark"
__helpurl__ = "https://pyrevitlabs.notion.site/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0"

# from pyrevit import revit

doc     = __revit__.ActiveUIDocument.Document
uidoc   = __revit__.ActiveUIDocument
app     = __revit__.Application
curview = doc.ActiveView

# -----------------Selection--------------------
selection_ids = uidoc.Selection.GetElementIds()
selected_elements = [doc.GetElement(id) for id in selection_ids]
   
# -------------------Functions----------------------
    
def get_target_solids(element):
    solids = []
    options = Options()
    options.DetailLevel = ViewDetailLevel.Fine
    geomElem = element.get_Geometry(options)
    for geomObj in geomElem:
        if isinstance(geomObj, Solid):
            solid = geomObj
            if solid.Faces.Size > 0 and solid.Volume > 0.0:
                solids.append(solid)
        elif isinstance(geomObj, GeometryInstance):
            geomInst = geomObj
            instGeomElem = geomInst.GetInstanceGeometry()
            for instGeomObj in instGeomElem:
                if isinstance(instGeomObj, Solid):
                    solid = instGeomObj
                    if solid.Faces.Size > 0 and solid.Volume > 0.0:
                        solids.append(solid)
    return solids

def get_target_edges(element):
    edges = []
    lengths = []
    num_face = []
    options = Options()
    options.DetailLevel = ViewDetailLevel.Fine
    geomElem = element.get_Geometry(options)
  
    for geomObj in geomElem:
        if isinstance(geomObj, Solid):
            solid = geomObj
            if solid.Faces.Size > 0 and solid.Volume > 0.0:
                sum_face.append(solid.Faces.Size)
                for face in solid.Faces:
                    for edge_loop in face.EdgeLoops:
                        edges.append(edge_loop)
                        for edge in edge_loop:
                            if face.FaceNormal.IsAlmostEqualTo(XYZ.BasisX) or face.FaceNormal.IsAlmostEqualTo(XYZ.BasisY):
                                length = edge.ApproximateLength
                                length_mm = UnitUtils.ConvertFromInternalUnits(length, UnitTypeId.Millimeters) 
                                lengths.append(length_mm)
                                num_face.append(face.Size)
        elif isinstance(geomObj, GeometryInstance):
            geomInst = geomObj
            instGeomElem = geomInst.GetInstanceGeometry()
            for instGeomObj in instGeomElem:
                if isinstance(instGeomObj, Solid):
                    solid = instGeomObj
                    if solid.Faces.Size > 0 and solid.Volume > 0.0:
                        num_face.append(solid.Faces.Size)
                        for face in solid.Faces:
                            for edge_loop in face.EdgeLoops:
                                edges.append(edge_loop)
                                for edge in edge_loop:
                                    try:
                                        if face.FaceNormal.IsAlmostEqualTo(XYZ.BasisX) or face.FaceNormal.IsAlmostEqualTo(XYZ.BasisY):
                                            length = edge.ApproximateLength
                                            length_mm = UnitUtils.ConvertFromInternalUnits(length, UnitTypeId.Millimeters) 
                                            lengths.append(length_mm)
                                    except: continue
    return edges, lengths, num_face

def get_parameter(element,parameter_name):
    isy_param = element.LookupParameter(parameter_name).AsValueString()
    return isy_param

def set_parameter(element, parameter_name, value):
    isy_param = element.LookupParameter(parameter_name)
    new_value = change_unit_string(value.ToString())
    isy_param.Set(new_value)

def change_unit_string(str):
    if len(str) < 4:
        new_str = str[:-3]+"0,"+str[-3:]
    else:
        new_str = str[:-3]+","+str[-3:]

    return new_str

    
edg = []
leng = []
n_face =[]
for elem in selected_elements:
    edg,leng, n_face = get_target_edges(elem)
    print("Lenght of all edges is {} and the longest length is {} and originates from a object with {} faces".format(leng,round(max(leng),0),n_face))

for para_elem in selected_elements:
    para = get_parameter(para_elem, 'ISY Mengde')
    print(para)

# -------------------Transaction----------------------

t= Transaction(doc,__title__)
t.Start()
for set_param_elem in selected_elements:
    edg,leng, n_face = get_target_edges(set_param_elem)
    set_parameter(set_param_elem, 'ISY Mengde', round(max(leng),0))

t.Commit()