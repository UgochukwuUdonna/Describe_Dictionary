# Name:        Dictionary demo
# Author:      frivera
# Created:     2-26-2021

# NOTE THAT THIS MODULE DOES NOT IMPORT THE arcpy MODULE

import sys, traceback
try:
    # THE GOAL IS TO PROVIDE A VALUE BASED ON ANOTHER VALUE OR KEY.
    cities = ["Austin", "Baltimore", "Cleveland", "Denver"]
    states = ["Texas", "Maryland", "Ohio", "Colorado"]
    print (f'IN WHAT STATE IS Baltimore: {states[cities.index("Baltimore")]}')
    print (f'IN WHAT STATE IS Denver: {states[cities.index("Denver")]}')
    print ()

    # # A BETTER APPROACH: USE A DICTIONARY (PAIRS OF KEYS AND VALUES)
    # statelookup = {"Denver":"Colorado", "Baltimore":"Maryland", "Cleveland":"Ohio", "Austin":"Texas"}
    # print (f'IN WHAT STATE IS Baltimore: {statelookup["Baltimore"]}')
    # # IN WHAT STATE IS Denver
    # print (f'IN WHAT STATE IS Denver: {statelookup["Denver"]}')
    # print ()
    # THE GOAL IS TO PROVIDE A VALUE BASED ON ANOTHER VALUE OR KEY.
    cities = ["Austin", "Baltimore", "Cleveland", "Denver"]
    states = ["Texas", "Maryland", "Ohio", "Colorado"]
    print (f'IN WHAT STATE IS Baltimore: {states[cities.index("Baltimore")]}')
    print (f'IN WHAT STATE IS Denver: {states[cities.index("Denver")]}')
    print ()
    #
    # # ANOTHER WAY OF CREATING THE DICTIONARY
    statelookup = {}
    statelookup["Denver"] = "Colorado"
    statelookup["Baltimore"] = "Maryland"
    statelookup["Cleveland"] = "Ohio"
    statelookup["Austin"] = "Texas"

    # # ITERATE THROUGH EACH DICTIONARY KEY AND PRINT ITS VALUE (UNSORTED KEYS)
    for aKey in statelookup:
         print ("The key: " + aKey + ", The Value: " + statelookup[aKey])
    print ()
    #
    # # ITERATE THROUGH EACH DICTIONARY KEY AND PRINT ITS VALUE (SORTED KEYS)
    theKeys = list(statelookup)
    # # OR
    # # theKeys = list(statelookup.keys()) #  .keys() RETURNS A "Dictionary View Object" dict_keys
    theKeys.sort()
    print (theKeys)
    #
    for aKey in theKeys:
        print ("The key: " + aKey + ", The value: " + statelookup[aKey])

except:

    # THIS IS NOT AN arcpy MODULE SO WE NEED LESS LINES TO TAKE CARE OF ERRORS BELOW
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n     " + str(sys.exc_info()[1])

    print (pymsg)

