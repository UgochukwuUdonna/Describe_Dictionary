# walk demo

# Created by: FELIPE RIVERA
# Created on: 2-22-2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    init_path = r'C:\Geog_432\Chapter_6\Sample Geodatabases'
    # Walk (top, {topdown}, {onerror}, {followlinks}, {datatype}, {type})
    for apath, subs, files in arcpy.da.Walk(init_path):
        # print (apath)
        # print (subs)
        # print (files)
        for asubfolder in subs:
            print (apath + '\\' + asubfolder)
        for afile in files:
            print (apath + '\\' + afile)
        print ('-------------------')
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
