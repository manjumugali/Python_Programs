"""
******************************************************************************
* Purpose:  Reading JSON File
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   27-01-2019
*
******************************************************************************
"""
import json

from OOPS_Utility.Test_Oops_Utility import InventoryDetails


class Inventory:
        try:
            with open("Inventory.json", "r") as file:   # open Json file
                json_file = file.read()                 # read json file
                file.close()                            # close file
                items = json.loads(json_file)           # convert json object to python object
                u = InventoryDetails()                  # creating object of InventoryDetails class
                u.inventoryDetails(items)               # invoking inventoryDetails class function
        except FileNotFoundError:
            print("File not Found")


if __name__ == "__main__":
    Inventory()