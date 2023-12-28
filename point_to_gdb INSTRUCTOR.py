# COPY POINT FCS TO A GDB

# Created by: FELIPE RIVERA
# Created on: 2-22-2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    # SET OVERWRITEOUTPUT TO TRUE
    arcpy.env.overwriteOutput = True
    # CREATE THE OUTPUT GDB
    path = r'C:\EsriPress\Python\Data\Austin-TX'
    gdb = 'points.gdb'
    # arcpy.management.CreateFileGDB(out_folder_path, out_name, {out_version})
    arcpy.CreateFileGDB_management(path, gdb)
    # SET THE WORKSPACE
    arcpy.env.workspace = path
    # GET LIST OF POINT FEATURE CLASSES
    points_list = arcpy.ListFeatureClasses(feature_type='Point')
    # print (points_list)
    # FOR EACH FC IN THE LIST
    for afc in points_list:
        # LET THE USER KNOW THE NAME OF THE FEATURECLASS BEING COPIED
        print (f'Copyting featureclass {afc} to gdb...')
        # COPY TO OUTPUT GDB
        # arcpy.management.CopyFeatures(in_features, out_feature_class, {config_keyword},
        #   {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})
        arcpy.CopyFeatures_management(afc, path + '\\' + gdb + '\\' + afc.replace('.shp', ''))



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
