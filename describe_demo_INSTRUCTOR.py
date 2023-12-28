# DESCRIBE DEMO

# Created by: FELIPE RIVERA
# Created on: 2-20-2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    r_dataset = r'C:\EsriPress\Python\Data\Colorado\Elevation'
    # Describe (value, {datatype})
    desc_object = arcpy.Describe(r_dataset)
    print (f'Catalog path: {desc_object.catalogPath}')
    print (f'Data type: {desc_object.dataType}')
    print (f'Band count: {desc_object.bandCount}')
    print (f'Compression type: {desc_object.compressionType}')
    print (f'Raster format: {desc_object.format}')
    print (f'Sensor type: {desc_object.sensorType}')

    r_dataset = r'C:\EsriPress\Python\Data\Colorado\tm.img'
    desc_dict = arcpy.da.Describe(r_dataset)
    print (f'Catalog path: {desc_dict["catalogPath"]}')
    print (f'Data type: {desc_dict["dataType"]}')
    print (f'Band count: {desc_dict["bandCount"]}')
    print (f'Compression type: {desc_dict["compressionType"]}')
    print (f'Raster format: {desc_dict["format"]}')
    print (f'Sensor type: {desc_dict["sensorType"]}')

    fc = r'C:\EsriPress\Python\Data\Alaska\airports.shp'
    desc_dict = arcpy.da.Describe(fc)
    print (f'FC data type: {desc_dict["dataType"]}')
    fld_list = desc_dict["fields"]
    fld_names = []
    for afield in fld_list:
        fld_names.append(afield.name)
    print (f'FC fields: {fld_names}')
    print (f'FC spat. reference: {desc_dict["spatialReference"].name}')
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
