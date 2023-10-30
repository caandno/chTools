# -*- coding: utf-8 -*-

__title__ = "IFC exporter"
__doc__ =  """Opens rvt file by predefined list of paths and export ifc by the IFC export view"""

# -----------------Imports--------------------
from Autodesk.Revit.DB import *
import sys
from pathlib import Path

__author__ = "Casper Helmark"
__helpurl__ = "https://pyrevitlabs.notion.site/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0"

from pyrevit import revit, forms
# from pyrevit.forms import WPFWindow

doc     = __revit__.ActiveUIDocument.Document
uidoc   = __revit__.ActiveUIDocument
app     = __revit__.Application

# -----------------Functions--------------------
#TODO Open rvt file by path, shall work with workshared files, preferably also cloud models

# Document OpenDocumentFile(
# 	ModelPath modelPath,
# 	OpenOptions openOptions
# )

# UIDocument OpenAndActivateDocument(
# 	ModelPath modelPath,
# 	OpenOptions openOptions,
# 	bool detachAndPrompt

def open_revit_file(file_path):
    options = app.DefaultOpenOptions()

    # Åpne Revit-filen
    doc = app.OpenAndActivateDocument(file_path, options, False)

    if doc:
        return doc  # Returnerer dokumentet hvis det ble åpnet
    else:
        return None

# Bruk funksjonen for å åpne en Revit-fil
file_path = "C:\Users\caand\OneDrive - Norconsult Group\Dev\ifcexporterRevit\test.rvt"
modelPath = ModelPathUtils.ConvertUserVisiblePathToModelPath(file_Path)
opened_doc = open_revit_file(modelPath)

if opened_doc:
    print("Revit-filen {} er åpnet.".format(file_path))
else:
    print("Kunne ikke åpne Revit-filen {}.".format(file_path))

#TODO Check if IFC export view exist, if not raise warning in log
#TODO Log action, succes, failure misiing view.
#TODO Close file without saving and relinquesh all

#------------------Input------------------------
#TODO Get list of paths to export
# filepaths = "C:\\Users\\caand\\OneDrive - Norconsult Group\\Dev\\ifcexporterRevit\\test.rvt"



# -------------------Transaction---------------------

# t= Transaction(doc,__title__)
# t.Start()

# t.Commit()

# ----------------End------------------.