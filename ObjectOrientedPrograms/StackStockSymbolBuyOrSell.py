"""
******************************************************************************
* Purpose:  Program To arrange Stock Symbol Purchased or Sold in a Stack implemented.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   30-01-2019
*
******************************************************************************
"""

import json
from OOPS_Utility.Test_Oops_Utility import StackStockSymbol


class StackStockSymbol:
    try:
        with open("BuyStock.json", "r") as file:  # open Json file
            json_file = file.read()  # read json file
            file.close()  # close file
            data = json.loads(json_file)  # convert json object to python object
            s1 = StackStockSymbol(data)  # creating object StackStockSymbol class and passing parameters
            s1.pushStockSymbols()  # on s1 object invoking stockReport() function
    except FileNotFoundError:
        print("File Not Found....!")
