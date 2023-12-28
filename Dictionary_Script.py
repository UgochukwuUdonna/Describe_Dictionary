# Dictionary_Script_Homework

# Created by: Ugochukwu Udonna Okonkwo
# Created on: 3/12/2023


print ("Importing modules...")
import sys, arcpy, traceback
try:
    # FOR EACH FOLDER IN THE PATH (FEATURE CLASSES ONLY)
    # Walk (top, {topdown}, {onerror}, {followlinks}, {datatype}, {type})
    init_path = r'C:\Geog_432\EsriPress\Python\Data'

    # Create dictionary
    d = {}
    for apath, subfolders, files in arcpy.da.Walk(init_path, datatype = 'FeatureClass'):
        # print(apath, subfolders, files)
        # FOR EACH FEATURE CLASS:
        for afile in files:
            # print(apath + '\\' + afile)
            # SAVE THE FEATURECLASS AND PROPERTY IN THE DICTIONARY
            try:
                desc = arcpy.da.Describe(apath + '\\' + afile)
                d[apath + '\\' + afile] = desc['spatialReference'].name
            except:
                print('error reading feature class ' + apath + '\\' + afile)

    # SHOW THE KEYS AND VALUES TO THE USER
    for akey in d:
        print(f'KEY: {akey}, VALUE: {d[akey]}')

except:

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n     " + str(sys.exc_info()[1])

    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    arcpy.AddError(msgs)
    arcpy.AddError(pymsg)

    print (msgs)
    print (pymsg)

    arcpy.AddMessage(arcpy.GetMessages(1))
    print (arcpy.GetMessages(1))
