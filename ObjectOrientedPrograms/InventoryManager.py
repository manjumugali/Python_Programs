"""
******************************************************************************
* Purpose:  Program To Inventory Management
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   29-01-2019
*
******************************************************************************
"""
import json

from OOPS_Utility.Test_Oops_Utility import InventoryManagement


class InventoryManager:
    try:
        with open("Inventory.json", "r") as file:       # open Json file
            json_file = file.read()                     # read json file
            file.close()                                # close file
            items = json.loads(json_file)               # convert json object to python object
            i1 = InventoryManagement(items)             # creating object InventoryManagement class and passing parameters
            i1.inventoryData()                          # on i1 object invoking inventoryData() function
    except FileNotFoundError:
        print("File not Found")